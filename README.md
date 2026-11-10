# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A writer's client sends `POST /submit` with JSON containing `text` and
   `creator_id`.
2. Flask's `/submit` handler validates the request (400 and a `rejected` log
   entry for missing or empty `text` or `creator_id`) and assigns a new
   `content_id`.
3. `detector.model_signal` tokenizes the text and asks the local GPT-2 model
   how predictable it is. It adds `model_score`, where a higher value means
   more predictable and therefore more AI-like to this signal.
4. `stylometry.style_signal` measures sentence-length variation, vocabulary
   repetition, and punctuation. It adds `style_score`, also oriented so a
   higher value means more AI-like.
5. `scoring.combine_signals` combines those two scores into one
   `combined_score`: the mean of the two, pulled halfway toward the lower
   one so that both signals must look AI-like for a high score.
6. `scoring.score_to_label` compares the combined score with the label bands
   and adds a machine-readable `guess` plus reader-facing `label` text.
7. `audit.log_decision` appends the scores, label, IDs, and status to the
   audit log. The handler returns the IDs, scores, guess, and label as JSON;
   the reader sees the label in that response.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal
### Signal one — the model signal
**What it measures:** `detector.model_signal` measures how predictable the
text is to a locally run GPT-2 language model. It converts perplexity into a
0-1 score; higher means more predictable and more AI-like to this signal.

**Why that might differ between human and AI writing:** A language model
generates likely next tokens, so generated text can have lower perplexity
(higher signal scores). Human writing can be less predictable because of
unusual word choices or abrupt shifts.

**What it can't see:** Predictability is not authorship. Plain, conventional
or second-language human writing can be easy for GPT-2 to predict and score
as AI-like. Conversely, unusual, dense, or heavily edited AI text can be hard
to predict and score as human-like. It cannot identify who wrote the text or
how it was produced.

### Signal two — the style signal

**What it measures:** `stylometry.style_signal` measures text shape using
sentence-length spread, type-token ratio (unique words divided by total
words), and punctuation density. The combined score must point in the same
direction as the model signal: higher means more AI-like.

**Why that might differ between human and AI writing:** Generated prose can
have more even sentence lengths, more repeated vocabulary, and a narrower
punctuation pattern. Human writing is often less uniform, so those three
measurements may differ.

**What it can't see:** These are surface measurements; they cannot understand
meaning, verify authorship, or tell whether a person edited generated text.
Short texts and topic or genre choices can change the measurements, and
someone can change sentence breaks, vocabulary, or punctuation without
changing the ideas. That can move this signal without changing who wrote the
text.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Take the mean of the two signals, then pull it halfway toward the
*lower* of the two. A high score needs both signals to look AI-like, so the
model signal alone (which over-flags plain human writing) can't produce an
accusation. When they disagree, the result lands in the middle or low.

**The numbers:** `mean = 0.50 * model_score + 0.50 * style_score`, then
`combined_score = 0.5 * mean + 0.5 * min(model_score, style_score)`
(`WEIGHT_*` and `LOWER_SIGNAL_PULL` in `config.py`). Style itself is
`0.45 * spread + 0.15 * vocabulary + 0.40 * punctuation`, each scaled 0-1.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:** My plain
human paragraph ("I went to the store yesterday...") scored model `0.83` (very
predictable to GPT-2) but style `0.39` (uneven sentences, some commas). A plain
mean gives `0.61`; the rule gives `0.50`, which is `unsure`, not an accusation.
The formal human paragraph also split: model `0.61`, style `0.03`, combined
`0.17`, so it reads as human.

**Calibration run (Milestone 4, 5 hand-picked texts, live through `/submit`):**

| Input | model | style | combined |
|---|---|---|---|
| clearly AI | 0.755 | 0.567 | 0.614 |
| clearly human | 0.274 | 0.051 | 0.107 |
| plain human | 0.831 | 0.389 | 0.499 |
| formal human | 0.611 | 0.026 | 0.172 |
| lightly edited AI | 0.389 | 0.010 | 0.105 |

The lightly edited AI paragraph scored as human on both signals: casual
wording, a dash and shorter sentences fooled both. That is a missed detection I
accept for now, since wrongly accusing a writer costs more. The gap between
clear AI (`0.61`) and plain human (`0.50`) is thin, and 5 samples is too few to
trust the constants. I tuned the scale constants in `stylometry.py` against
these same samples, so they are optimistic.

### The false-positive case that sets the policy

Imagine a real writer, especially one writing in a second language, using
short, common words and straightforward sentences. GPT-2 finds the writing
predictable. In one illustrative case, the model score is `0.90` and the
style score is `0.72`; the equal-weight combined score is `0.81`. These
numbers are an example of the path, not a measured result from the unfinished
signals.

With the old Milestone 1 AI cutoff of `0.80`, that writer would receive the `ai` guess and
the label, "This text appears likely to have been written by AI." That is a
false positive, not proof of misconduct. The writer can submit
`POST /appeal` with the returned `content_id` and an explanation. The service
records an `under_review` appeal without overwriting the original decision;
a person must review it. The wide unsure band and the high AI cutoff are
intended to make this costly mistake less likely, even though they allow more
AI-written text to remain uncertain.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00-0.35 | This text appears more consistent with human writing. |
| unsure | above 0.35 and below 0.55 | We can't reliably tell from this text alone. If this is your work, you can ask for a human review. |
| high-confidence AI | 0.55-1.00 | This text appears likely to have been written by AI. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

It says the system cannot reliably tell, rather than blaming the writer. It
also points to a next step instead of leaving someone with a score and no
recourse.

**Reachability check (live through `/submit`):** clearly AI text scored `0.614`
and got the AI label; plain human writing scored `0.499` and got "unsure";
clearly human writing scored `0.107` and got the human label. All three are
reachable, and `scoring.label_ranges()` shows no gap between the bands.

**Threshold decision:** The human cutoff stays at `0.35`. In Milestone 1 I
proposed an AI cutoff of `0.80`, but calibration showed the combined score for
clearly AI text tops out near `0.61`, so `0.80` would make the AI label
unreachable. `config.py` and the table above now use `0.55`. That still keeps plain human writing
(`0.50`) in `unsure`, though only narrowly.

---

## Endpoint Contract

These are the design contracts for the two endpoints being built; both route
handlers are still TODOs. Successful responses use HTTP `200` and JSON.
Validation failures use a non-200 status with
`{"error": "<code>", "message": "<plain-language explanation>"}`.

### `POST /submit`

**Request JSON**

| Field | Type | Required | Meaning |
|---|---|---:|---|
| `text` | non-empty string | Yes | Text to score. It must contain enough text for the model signal to run (at least three model tokens). |
| `creator_id` | non-empty string | Yes | Caller-provided ID used to associate the submission and its audit entries with the creator. |

**Successful response JSON**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | Unique ID for this submission; use it to appeal. |
| `guess` | string | One of `human`, `unsure`, or `ai`. |
| `confidence` | number, 0-1 | Combined AI-likelihood score; this is a score, not a calibrated probability. |
| `label` | string | Exact reader-facing sentence for the selected guess. |
| `model_score` | number, 0-1 | `detector.model_signal` result; higher means more AI-like. |
| `style_score` | number, 0-1 | `stylometry.style_signal` result; higher means more AI-like. |

`confidence` is the response name for the combined score. The audit entry
stores the same value as `combined_score`, along with `timestamp`,
`content_id`, `creator_id`, `guess`, `model_score`, `style_score`, `label`,
and `status` (`decided`).

### `POST /appeal`

**Request JSON**

| Field | Type | Required | Meaning |
|---|---|---:|---|
| `content_id` | non-empty string | Yes | ID returned by `/submit` for the decision being challenged. |
| `reasoning` | non-empty string | Yes | The writer's explanation of why they believe the decision is wrong. |

**Successful response JSON**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | The appealed submission. |
| `status` | string | `under_review`; the original decision remains in the append-only audit log. |
| `message` | string | Confirmation that the appeal was recorded for human review. |

An appeal for an unknown `content_id` returns HTTP `404`; missing or
malformed required fields return HTTP `400`. An appeal records a review
request; it does not automatically rescore the text or overturn the result.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "I went to the store yesterday to buy some groceries. The prices were higher than I expected, so I only bought the essentials. I got milk, bread, and eggs. It was a pretty normal trip overall. Then I went home and made dinner.", "creator_id": "m5_plain_human"}'
```

```json
{
  "confidence": 0.4993,
  "content_id": "932fb5e7-9956-4214-8068-018a9a19e78e",
  "guess": "unsure",
  "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review.",
  "model_score": 0.8305,
  "style_score": 0.3889
}
```

(`confidence` is the combined score.) A bad input (`{"text": "", "creator_id": "x"}`)
returns HTTP `400` and is logged as a `rejected` entry.

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "932fb5e7-9956-4214-8068-018a9a19e78e", "reasoning": "I wrote this myself about a trip to the store."}'
```

```json
{
  "content_id": "932fb5e7-9956-4214-8068-018a9a19e78e",
  "message": "Your appeal was recorded and will be reviewed by a person.",
  "status": "under_review"
}
```

An unknown `content_id` returns `404`; a missing `reasoning` returns `400`.

**What the log shows afterwards** (both entries for that `content_id`; the
original decision is untouched and the appeal sits after it)

```bash
$ curl "http://127.0.0.1:5000/log"
```

```json
{
  "entries": [
    {
      "timestamp": "2026-11-04T03:19:36+00:00",
      "content_id": "932fb5e7-9956-4214-8068-018a9a19e78e",
      "creator_id": "m5_plain_human",
      "guess": "unsure",
      "model_score": 0.8305,
      "style_score": 0.3889,
      "combined_score": 0.4993,
      "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review.",
      "status": "decided"
    },
    {
      "timestamp": "2026-11-04T03:19:36+00:00",
      "content_id": "932fb5e7-9956-4214-8068-018a9a19e78e",
      "creator_id": "m5_plain_human",
      "event": "appeal",
      "status": "under_review",
      "reasoning": "I wrote this myself about a trip to the store."
    }
  ]
}
```

(Other entries trimmed for length.)

---

## How I Used AI

**Moment 1**

- *What I asked for:* A second signal in `stylometry.py` (sentence-length
  spread, vocabulary variety, punctuation density) and a combining rule in
  `scoring.py::combine_signals`.
- *What came back:* Working measures scaled 0-1 and a rule that takes the mean
  of the two signals. On my first calibration run the plain human paragraph
  scored `0.83` on the model signal, higher than clearly AI text, and the
  lightly edited AI paragraph scored as human.
- *What I changed:* I re-scaled the style constants against my samples,
  down-weighted vocabulary variety because it barely separated anything, and
  changed the rule to pull the mean halfway toward the lower signal so that the
  model signal alone can't produce an AI label. I also lowered `AI_THRESHOLD`
  from my planned `0.80` to `0.55`, because clear AI text only reached `0.61`
  and `0.80` made the AI label unreachable.

**Moment 2**

- *What I asked for:* The `/submit` and `/appeal` routes, built in stages with
  a hardcoded response first.
- *What came back:* Routes that validate input (400 on bad requests), log every
  decision, and return both signal scores. The appeal route returned 404 for
  unknown IDs and appended an `under_review` entry without touching the original
  decision.
- *What I changed:* I checked behaviour myself with `curl` and the log rather
  than trusting the code: the first run of `python app.py` failed because
  flask is only installed in `.venv`, so I ran everything through
  `.venv\Scripts\python.exe`. I also noted that the tuned constants are
  optimistic because they were fitted to the same five samples I tested on.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

Full table: `results/attack_run_2026-11-09_2018_before.md`. **Held 32, broke 24, of 56.**

How I marked them: an attack **held** if the service did the right thing for
that input (rejected junk with a 4xx, rate-limited the flood, called genuine
human writing human or unsure, called AI text AI). It **broke** if it got
what it was going for. For evasion/injection rows the text is AI-written, so
anything short of an `ai` guess counts as evaded. For `false_positive` rows
an `ai` guess is the break; `unsure` held.

| Family | Held | Broke | Broke rows |
|---|---|---|---|
| evasion (10) | 1 | 9 | EV01–EV09 (only EV10, repeated stanzas, was caught at 0.729) |
| false_positive (8) | 3 | 5 | FP02 0.733, FP03 0.730, FP04 0.633, FP05 0.677, FP06 0.586 all called `ai` |
| prompt_injection (6) | 2 | 4 | PI01 unsure, PI02 human, PI03 unsure, PI05 human; PI04, PI06 held |
| malformed (20) | 14 | 6 | MF03 control chars → human, MF04 punctuation → human, MF05 one long word → ai, MF06 emoji → ai 0.998, MF07 RTL script → ai, MF08 60k chars accepted with no size cap |
| flood_same_creator (12) | 12 | 0 | first 5 got `200`, FL01_06–12 got `429` |

Notes: RQ10 and RQ11 returned `429` (no usable `creator_id`, so they counted
against my address) and never reached the route, so I marked them held but
they did not test my input handling. For PI01–PI03/PI05 there is no evidence
the service "obeyed" the injected instruction (it never reads text as
instructions); the low scores come from the signals, but the outcome is still
a miss. EV05 is a heavily human-edited AI draft, so "human" is arguably fair.

**Ten audit log entries from the run**

Pulled from `GET /log` (`results/audit_extract.json`).

```json
{"timestamp":"2026-11-10T01:17:56+00:00","content_id":"0fdf9876-1699-45a1-9181-62bb04dd8be9","creator_id":"attacker_FP03","guess":"ai","model_score":0.8051,"style_score":0.7046,"combined_score":0.7297,"label":"This text appears likely to have been written by AI.","status":"decided"}
{"timestamp":"2026-11-10T01:17:56+00:00","content_id":"c1775902-87a3-4b7c-8687-9806eca5d14d","creator_id":"attacker_FP02","guess":"ai","model_score":0.7387,"style_score":0.7311,"combined_score":0.733,"label":"This text appears likely to have been written by AI.","status":"decided"}
{"timestamp":"2026-11-10T01:17:54+00:00","content_id":"1bfdf34c-72dc-474e-a443-aad657e73f7d","creator_id":"attacker_EV01","guess":"human","model_score":0.1635,"style_score":0.5767,"combined_score":0.2668,"label":"This text appears more consistent with human writing.","status":"decided"}
{"timestamp":"2026-11-10T01:17:57+00:00","content_id":"4e0b2b4b-cd55-4a54-b491-55ef04a18cb4","creator_id":"attacker_PI02","guess":"human","model_score":0.2044,"style_score":0.2222,"combined_score":0.2088,"label":"This text appears more consistent with human writing.","status":"decided"}
{"timestamp":"2026-11-10T01:17:58+00:00","content_id":"2f39cea1-8ea4-4387-827a-f5a922f18336","creator_id":"attacker_PI05","guess":"human","model_score":0.6401,"style_score":0.0257,"combined_score":0.1793,"label":"This text appears more consistent with human writing.","status":"decided"}
{"timestamp":"2026-11-10T01:17:58+00:00","content_id":"538f9c01-c11d-40f9-8450-f92c66532638","creator_id":"attacker_MF03","guess":"human","model_score":0.0,"style_score":0.7273,"combined_score":0.1818,"label":"This text appears more consistent with human writing.","status":"decided"}
{"timestamp":"2026-11-10T01:17:59+00:00","content_id":"612eae97-0080-45ca-b4f4-50826ce9cb79","creator_id":"attacker_MF06","guess":"ai","model_score":0.9969,"style_score":1.0,"combined_score":0.9977,"label":"This text appears likely to have been written by AI.","status":"decided"}
{"timestamp":"2026-11-10T01:18:00+00:00","creator_id":"attacker_RQ12","event":"rejected","status":"rejected","reason":"invalid_text"}
{"timestamp":"2026-11-10T01:18:00+00:00","creator_id":"unknown","event":"rejected","status":"rejected","reason":"rate_limited","limit":"5 per 1 minute"}
{"timestamp":"2026-11-10T01:18:00+00:00","creator_id":"attacker_flood","event":"rejected","status":"rejected","reason":"rate_limited","limit":"5 per 1 minute"}
```

What they show: FP02/FP03 are real-style human writing labelled AI; PI05 has
`model_score` 0.64 but `style_score` 0.026, and the style signal alone pulled
it to "human"; MF03 has `model_score` 0.0 on junk; MF06 emoji scored 0.998;
the last three are rejections (route 400, a rate-limited unknown caller, and
the flood).

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

**FP03**, a non-native English speaker writing carefully about their first
month in a new country, got `guess: ai`, combined 0.7297, label "likely
written by AI". Both signals agreed (model 0.805, style 0.705), so it isn't a
one-signal fluke: plain, short, regular sentences are exactly what both
signals read as machine-like. That writer did nothing wrong and is told
otherwise by the system, and the people most exposed are those writing in a
second language. The appeal route exists, but it only helps after the label
has already been shown.



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing flagged as AI | ≤ 1 of 10 per run | 0/10 | 0/10 | 0/10 | MET |
| 2. Score spread, AI median minus own-writing median | ≥ 0.30 | 0.246 | 0.246 | 0.246 | MISSED |
| 3. All three labels reachable | 3 of 3 | 3/3 | 3/3 | 3/3 | MET |
| 4. Valid appeals recorded, original decision intact | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Bad input → 400/413, no decision, rejection logged | 5 of 5 | 4/5 | 4/5 | 4/5 | MISSED |

Full output: `results/run_2026-11-09_2108_before.md`. Scenarios live in
`scenarios.py`; produced by `run_eval.py::main`. Criteria 4 and 5 can't be
expressed as "send text and read the response", so I extended `run_eval.py`
with a `"run"` hook: `scenarios.py::_run_appeals` submits then appeals and
checks the audit log, and `scenarios.py::_run_bad_input` checks the status,
that no decision entry exists, and that a rejection entry exists.


**Real output from one trial** (Trial 1 of `results/run_2026-11-09_2108_before.md`,
produced by `app.py::submit` and `app.py::appeal`, recorded by
`run_eval.py::main`; `sent` previews removed, excerpts of each scenario):

*Criterion 1: first three of my own pieces*

```json
[
  {"status": 200, "guess": "human", "confidence": 0.3243, "model_score": 0.3036, "style_score": 0.3865, "label": "This text appears more consistent with human writing."},
  {"status": 200, "guess": "human", "confidence": 0.1422, "model_score": 0.36, "style_score": 0.0696, "label": "This text appears more consistent with human writing."},
  {"status": 200, "guess": "unsure", "confidence": 0.3964, "model_score": 0.5689, "style_score": 0.3389, "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review."}
]
```

*Criterion 2: AI pieces 1, 2 and 5. Medians over all five were AI 0.451
(scores 0.4222, 0.451, 0.4164, 0.5306, 0.5784) vs own writing 0.2052
(0.3243, 0.1422, 0.3964, 0.119, 0.1968, 0.2111, 0.3932, 0.3789, 0.1993, 0.1866)*

```json
[
  {"status": 200, "guess": "unsure", "confidence": 0.4222, "model_score": 0.7698, "style_score": 0.3063, "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review."},
  {"status": 200, "guess": "unsure", "confidence": 0.451, "model_score": 0.7907, "style_score": 0.3377, "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review."},
  {"status": 200, "guess": "ai", "confidence": 0.5784, "model_score": 0.9067, "style_score": 0.469, "label": "This text appears likely to have been written by AI."}
]
```

*Criterion 3: one result per label*

```json
[
  {"status": 200, "guess": "unsure", "confidence": 0.4222, "model_score": 0.7698, "style_score": 0.3063, "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review."},
  {"status": 200, "guess": "ai", "confidence": 0.5982, "model_score": 0.8746, "style_score": 0.5061, "label": "This text appears likely to have been written by AI."},
  {"status": 200, "guess": "human", "confidence": 0.119, "model_score": 0.3327, "style_score": 0.0477, "label": "This text appears more consistent with human writing."}
]
```

*Criterion 4: two of the five appeals*

```json
[
  {"passed": true, "submit_status": 200, "appeal_status": 200,
   "appeal_body": {"content_id": "3e9892e4-ffab-4201-afa8-4264b9cd0c04", "message": "Your appeal was recorded and will be reviewed by a person.", "status": "under_review"},
   "decision_entries": 1, "appeal_entries": 1},
  {"passed": true, "submit_status": 200, "appeal_status": 200,
   "appeal_body": {"content_id": "ac05341e-5758-4116-a546-80fba934736b", "message": "Your appeal was recorded and will be reviewed by a person.", "status": "under_review"},
   "decision_entries": 1, "appeal_entries": 1}
]
```

*Criterion 5: a pass (null text) and the failure (over 50,000 characters)*

```json
[
  {"passed": true, "kind": "null_text", "status": 400, "decision_entries": 0, "rejection_entries": 1,
   "body": {"error": "invalid_input", "message": "`text` must be a non-empty string."}},
  {"passed": false, "kind": "over_50000_chars", "status": 200, "decision_entries": 1, "rejection_entries": 0,
   "body": {"confidence": 0.9981, "content_id": "2417d4c7-cdec-41ad-adb9-fec56d93058c", "guess": "ai", "label": "This text appears likely to have been written by AI.", "model_score": 0.9975, "style_score": 1.0}}
]
```

**Diagnoses**

- **Criterion 5 (route):** `app.py::submit` has no length check, so a 50,005-character
  body goes straight to scoring: it returned `200`, was scored `ai` at 0.998, wrote
  a decision entry and no rejection. The route stage needs a size cap returning
  413 plus `audit.log_rejection`. Also a cost risk: it ran the model on oversize input.
- **Criterion 2 (signal one / combining rule):** the AI pieces' `model_score`
  was high (0.77–0.91) but `style_score` stayed 0.31–0.47, and the combining rule
  pulls toward the lower signal (`LOWER_SIGNAL_PULL = 0.5`), so the combined
  gap is 0.246. Stylometry doesn't separate short, generic AI paragraphs from
  casual human writing, so signal two is the weak stage.

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
