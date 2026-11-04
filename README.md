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
2. Flask's `/submit` handler validates the request, assigns a new `content_id`,
   and keeps the text and creator tied to that submission.
3. `detector.model_signal` tokenizes the text and asks the local GPT-2 model
   how predictable it is. It adds `model_score`, where a higher value means
   more predictable and therefore more AI-like to this signal.
4. `stylometry.style_signal` measures sentence-length variation, vocabulary
   repetition, and punctuation. It adds `style_score`, also oriented so a
   higher value means more AI-like.
5. `scoring.combine_signals` combines those two scores into one
   `combined_score`; disagreement between signals should contribute
   uncertainty rather than being hidden.
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

**The rule:** Take the arithmetic mean so neither signal dominates by default.
When they disagree, the mean moves toward the middle; the disagreement is
uncertainty, not a reason to let either signal decide alone.

**The numbers:** `combined_score = 0.50 * model_score + 0.50 * style_score`.
For example, model `0.90` and style `0.10` produce `0.50`, which is `unsure`
under the proposed label bands below.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:** A
plainly written human paragraph might be very predictable to GPT-2 but have
uneven sentence lengths and punctuation. If the model score is `0.90` and the
style score is `0.10`, the mean is `0.50`; the system returns `unsure` instead
of making a high-confidence accusation.

### The false-positive case that sets the policy

Imagine a real writer, especially one writing in a second language, using
short, common words and straightforward sentences. GPT-2 finds the writing
predictable. In one illustrative case, the model score is `0.90` and the
style score is `0.72`; the equal-weight combined score is `0.81`. These
numbers are an example of the path, not a measured result from the unfinished
signals.

With the proposed AI cutoff of `0.80`, that writer receives the `ai` guess and
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
| unsure | above 0.35 and below 0.80 | We can't reliably tell from this text alone. If this is your work, you can ask for a human review. |
| high-confidence AI | 0.80-1.00 | This text appears likely to have been written by AI. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

It says the system cannot reliably tell, rather than blaming the writer. It
also points to a next step instead of leaving someone with a score and no
recourse.

**Threshold decision:** These are proposed Milestone 1 thresholds, not the
starter's current runtime settings (`0.35` human and `0.65` AI in
`config.py`). I propose keeping the human cutoff at `0.35` and raising the AI
cutoff to `0.80`; a real writer should not receive a high-confidence AI label
from a borderline score. Milestone 4 calibration must test this tradeoff.

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
  -d '{"text": "Honestly? I burned the toast again, swore at the smoke alarm, and ended up eating cold cereal on my fire escape while a pigeon eyed me like I owed it rent.", "creator_id": "tanveer"}'
```

```json
{
  "confidence": 0.0,
  "content_id": "e2bebf3d-ae58-46c7-9a12-f6f3c27354ae",
  "guess": "unsure",
  "label": "PLACEHOLDER",
  "model_score": 0.1777,
  "style_score": null
}
```

*(Milestone 3 state: only the model signal is real; `style_score`, confidence,
guess and label are placeholders until Milestones 4 and 5.)*

A bad input (`{"text": "", "creator_id": "x"}`) returns HTTP `400` and is logged
as a `rejected` entry.

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": null,
      "content_id": "e2bebf3d-ae58-46c7-9a12-f6f3c27354ae",
      "creator_id": "tanveer",
      "guess": "unsure",
      "label": "PLACEHOLDER",
      "model_score": 0.1777,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-11-04T03:11:04+00:00"
    },
    {
      "creator_id": "x",
      "event": "rejected",
      "reason": "invalid_text",
      "status": "rejected",
      "timestamp": "2026-11-04T03:11:04+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

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

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



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
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

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
