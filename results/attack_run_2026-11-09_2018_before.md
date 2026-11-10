# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 20:18
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `1bfdf34c-72dc-474e-a443-aad657e73f7d` | human | 0.267 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `242c24fc-be3f-4fe9-a24b-c6fe19b6883f` | unsure | 0.388 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c3d07bba-9c88-4efe-a7e6-970fda66c6d7` | human | 0.329 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `7b5c10f4-5fab-4f8f-ac31-6ef6b517c876` | unsure | 0.542 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `9f38d43d-fac1-4e69-806a-6f32553e67bd` | human | 0.226 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c5a0e4f5-50f7-403f-a8ba-55976a018d9b` | unsure | 0.458 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `0357979d-a0d4-4e84-9a79-ce6ec79bad30` | human | 0.327 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `3b0e0354-e55e-4676-b4b2-387bc26f8570` | human | 0.333 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `d6f96972-45a1-4b8f-b28f-5c93bcc9894c` | unsure | 0.375 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `be4e6e22-a916-40d3-8221-8e5f5077892d` | ai | 0.729 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `ac8b154a-c857-4d19-805c-79764f625a16` | unsure | 0.537 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `c1775902-87a3-4b7c-8687-9806eca5d14d` | ai | 0.733 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `0fdf9876-1699-45a1-9181-62bb04dd8be9` | ai | 0.730 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `9fcd7fdf-92d1-4667-8b6e-094f694bc163` | ai | 0.633 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `f4996b98-9a6e-42cc-afa5-e450c0e38048` | ai | 0.677 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `2e5f3b0a-55a8-4997-bd8e-22504cca498f` | ai | 0.586 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `9f9b8e3e-5381-4504-80f7-88e1553e9aec` | unsure | 0.531 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `407d39ea-348a-4f1d-8366-e6d2ace9bb63` | unsure | 0.357 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `df2293fe-34bc-44c2-a22c-e4c1babe4b12` | unsure | 0.425 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `4e0b2b4b-cd55-4a54-b491-55ef04a18cb4` | human | 0.209 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `2d83e302-b511-4b74-bb7e-009ffba6abe0` | unsure | 0.414 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `0143f70b-3e93-466c-adf2-71605b7b3e4c` | human | 0.308 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `2f39cea1-8ea4-4387-827a-f5a922f18336` | human | 0.179 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `6600acde-bf56-4931-9a46-8744d63e68f0` | unsure | 0.536 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `538f9c01-c11d-40f9-8450-f92c66532638` | human | 0.182 |  |
| MF04 | malformed | text is only punctuation | 200 | `5f810d78-71e6-4287-9336-cdf483a67650` | human | 0.258 |  |
| MF05 | malformed | text is a very long single word | 200 | `5e34c41f-ab07-4149-b522-c82d6d5a52da` | ai | 0.795 |  |
| MF06 | malformed | text is emoji only | 200 | `612eae97-0080-45ca-b4f4-50826ce9cb79` | ai | 0.998 |  |
| MF07 | malformed | text is right-to-left script | 200 | `d669fe66-a12a-45b9-95b4-0d2a0aad6dda` | ai | 0.930 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `fcfa041c-42db-4e9f-859c-24f13113878e` | ai | 0.650 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `738c6468-0948-4ed9-967a-9eddee2b492d` | human | 0.203 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5434de94-bdb3-4069-9521-f24292fcf13d` | human | 0.203 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `37e58a97-0eac-45ac-a4e0-506cfe3ebccc` | human | 0.203 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ea578fad-0f66-4bd6-b5e2-d57cf74ce691` | human | 0.203 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bd735101-fcd1-49a2-a5f7-f1ff40ecbb19` | human | 0.203 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "1bfdf34c-72dc-474e-a443-aad657e73f7d",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.2668,
  "model_score": 0.1635,
  "style_score": 0.5767,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "242c24fc-be3f-4fe9-a24b-c6fe19b6883f",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.3875,
  "model_score": 0.5943,
  "style_score": 0.3185,
  "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c3d07bba-9c88-4efe-a7e6-970fda66c6d7",
  "creator_id": "attacker_EV03",
  "guess": "human",
  "confidence": 0.329,
  "model_score": 0.6662,
  "style_score": 0.2166,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "7b5c10f4-5fab-4f8f-ac31-6ef6b517c876",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5423,
  "model_score": 0.6114,
  "style_score": 0.5192,
  "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "9f38d43d-fac1-4e69-806a-6f32553e67bd",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2264,
  "model_score": 0.3212,
  "style_score": 0.1948,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "c5a0e4f5-50f7-403f-a8ba-55976a018d9b",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4579,
  "model_score": 0.5727,
  "style_score": 0.4196,
  "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "0357979d-a0d4-4e84-9a79-ce6ec79bad30",
  "creator_id": "attacker_EV07",
  "guess": "human",
  "confidence": 0.3274,
  "model_score": 0.5862,
  "style_score": 0.2411,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "3b0e0354-e55e-4676-b4b2-387bc26f8570",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3327,
  "model_score": 0.2452,
  "style_score": 0.5954,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "d6f96972-45a1-4b8f-b28f-5c93bcc9894c",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.3752,
  "model_score": 0.7042,
  "style_score": 0.2655,
  "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "be4e6e22-a916-40d3-8221-8e5f5077892d",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.7289,
  "model_score": 0.9792,
  "style_score": 0.6455,
  "label": "This text appears likely to have been written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "ac8b154a-c857-4d19-805c-79764f625a16",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5373,
  "model_score": 0.6175,
  "style_score": 0.5106,
  "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "c1775902-87a3-4b7c-8687-9806eca5d14d",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.733,
  "model_score": 0.7387,
  "style_score": 0.7311,
  "label": "This text appears likely to have been written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "0fdf9876-1699-45a1-9181-62bb04dd8be9",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7297,
  "model_score": 0.8051,
  "style_score": 0.7046,
  "label": "This text appears likely to have been written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "9fcd7fdf-92d1-4667-8b6e-094f694bc163",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6335,
  "model_score": 0.8329,
  "style_score": 0.567,
  "label": "This text appears likely to have been written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "f4996b98-9a6e-42cc-afa5-e450c0e38048",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.6775,
  "model_score": 0.8005,
  "style_score": 0.6365,
  "label": "This text appears likely to have been written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "2e5f3b0a-55a8-4997-bd8e-22504cca498f",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.586,
  "model_score": 0.8814,
  "style_score": 0.4875,
  "label": "This text appears likely to have been written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "9f9b8e3e-5381-4504-80f7-88e1553e9aec",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5312,
  "model_score": 0.8816,
  "style_score": 0.4144,
  "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "407d39ea-348a-4f1d-8366-e6d2ace9bb63",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3568,
  "model_score": 0.3223,
  "style_score": 0.4603,
  "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "df2293fe-34bc-44c2-a22c-e4c1babe4b12",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.425,
  "model_score": 0.4625,
  "style_score": 0.4125,
  "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "4e0b2b4b-cd55-4a54-b491-55ef04a18cb4",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2088,
  "model_score": 0.2044,
  "style_score": 0.2222,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "2d83e302-b511-4b74-bb7e-009ffba6abe0",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4139,
  "model_score": 0.5943,
  "style_score": 0.3538,
  "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "0143f70b-3e93-466c-adf2-71605b7b3e4c",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.3085,
  "model_score": 0.4998,
  "style_score": 0.2447,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "2f39cea1-8ea4-4387-827a-f5a922f18336",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.1793,
  "model_score": 0.6401,
  "style_score": 0.0257,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "6600acde-bf56-4931-9a46-8744d63e68f0",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5358,
  "model_score": 0.5583,
  "style_score": 0.5283,
  "label": "We can't reliably tell from this text alone. If this is your work, you can ask for a human review.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "538f9c01-c11d-40f9-8450-f92c66532638",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.1818,
  "model_score": 0.0,
  "style_score": 0.7273,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "5f810d78-71e6-4287-9336-cdf483a67650",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2584,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "5e34c41f-ab07-4149-b522-c82d6d5a52da",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7949,
  "model_score": 0.9976,
  "style_score": 0.7273,
  "label": "This text appears likely to have been written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "612eae97-0080-45ca-b4f4-50826ce9cb79",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9977,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "This text appears likely to have been written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "d669fe66-a12a-45b9-95b4-0d2a0aad6dda",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9298,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "This text appears likely to have been written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "fcfa041c-42db-4e9f-859c-24f13113878e",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.6497,
  "model_score": 0.9876,
  "style_score": 0.537,
  "label": "This text appears likely to have been written by AI.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "738c6468-0948-4ed9-967a-9eddee2b492d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2033,
  "model_score": 0.0287,
  "style_score": 0.7273,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "5434de94-bdb3-4069-9521-f24292fcf13d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2033,
  "model_score": 0.0287,
  "style_score": 0.7273,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "37e58a97-0eac-45ac-a4e0-506cfe3ebccc",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2033,
  "model_score": 0.0287,
  "style_score": 0.7273,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "ea578fad-0f66-4bd6-b5e2-d57cf74ce691",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2033,
  "model_score": 0.0287,
  "style_score": 0.7273,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "bd735101-fcd1-49a2-a5f7-f1ff40ecbb19",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2033,
  "model_score": 0.0287,
  "style_score": 0.7273,
  "label": "This text appears more consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
