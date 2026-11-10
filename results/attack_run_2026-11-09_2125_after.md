# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 21:25
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `0dddca86-1d67-4e1e-a7a6-1f412d17b11c` | human | 0.267 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `b9704678-9aa1-44da-b2a6-12beef160a64` | unsure | 0.388 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `56e3a401-59ae-4ca0-89f0-1c7dba19b73e` | human | 0.329 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `1921d482-e8d7-4d4c-bfa3-12208f03d895` | unsure | 0.542 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `2f80eb54-fce5-4122-a86a-c3be760afc0e` | human | 0.226 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `a2a2e70c-5aa0-4597-ba92-dbbdfd3d1150` | unsure | 0.458 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `062f0684-95a3-4394-883c-5140b8a32db0` | human | 0.327 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `165e7b47-6205-4481-8806-cfd3db73080e` | human | 0.333 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `6d740e61-bb89-4dc6-8c95-e43ea3f66901` | unsure | 0.375 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `b6eea54d-e5aa-4c39-b6b6-5eca03fdf44c` | ai | 0.729 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `15caf25a-a259-4b34-bd65-3d470c0154eb` | unsure | 0.537 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `e3a0d7c0-b8ca-4b74-b396-f3693d05c51f` | ai | 0.733 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `4bf524f4-6c4b-4250-a8f8-cdea8e12d308` | ai | 0.730 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `215d9730-bf5c-4ada-ae40-10dae502b9ed` | ai | 0.633 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `060a4fde-8600-4d1a-9e9f-85a415bce3a0` | ai | 0.677 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `c9d3d26f-fed6-4d24-8df0-c8ef7fcebea6` | ai | 0.586 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `f605639b-3fc6-4efd-b24f-cba5af134a74` | unsure | 0.531 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `32c037fb-8db1-4cb4-b5d5-8716c7ec9e01` | unsure | 0.357 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `33be49ab-c10b-49ea-819b-84120362f058` | unsure | 0.425 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `cac5d4c0-1ae6-4a92-a978-463d045b7a37` | human | 0.209 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `24ef02b0-851d-4124-af71-b8247c503425` | unsure | 0.414 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `fe2c9178-e286-4070-b6df-b6c03f21ba86` | human | 0.308 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `01378724-988c-42fb-9fd4-a5566c2b7ef5` | human | 0.179 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `804e078f-b7c0-41b5-9084-d7f240b44ab6` | unsure | 0.536 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d9dbdcd0-0d91-4a7c-b5d2-7e7edd06b672` | human | 0.203 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e0c2426a-7ef0-4bfc-a9da-fa59a2fd7e73` | human | 0.203 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `072a53e2-f5d6-4452-9dab-68d4e3f33c4b` | human | 0.203 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9cfe335b-a178-423f-b880-509b0302c3e1` | human | 0.203 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f7580f2d-8016-41cf-970d-39447b6e9e6d` | human | 0.203 |  |
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
  "content_id": "0dddca86-1d67-4e1e-a7a6-1f412d17b11c",
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
  "content_id": "b9704678-9aa1-44da-b2a6-12beef160a64",
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
  "content_id": "56e3a401-59ae-4ca0-89f0-1c7dba19b73e",
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
  "content_id": "1921d482-e8d7-4d4c-bfa3-12208f03d895",
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
  "content_id": "2f80eb54-fce5-4122-a86a-c3be760afc0e",
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
  "content_id": "a2a2e70c-5aa0-4597-ba92-dbbdfd3d1150",
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
  "content_id": "062f0684-95a3-4394-883c-5140b8a32db0",
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
  "content_id": "165e7b47-6205-4481-8806-cfd3db73080e",
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
  "content_id": "6d740e61-bb89-4dc6-8c95-e43ea3f66901",
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
  "content_id": "b6eea54d-e5aa-4c39-b6b6-5eca03fdf44c",
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
  "content_id": "15caf25a-a259-4b34-bd65-3d470c0154eb",
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
  "content_id": "e3a0d7c0-b8ca-4b74-b396-f3693d05c51f",
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
  "content_id": "4bf524f4-6c4b-4250-a8f8-cdea8e12d308",
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
  "content_id": "215d9730-bf5c-4ada-ae40-10dae502b9ed",
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
  "content_id": "060a4fde-8600-4d1a-9e9f-85a415bce3a0",
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
  "content_id": "c9d3d26f-fed6-4d24-8df0-c8ef7fcebea6",
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
  "content_id": "f605639b-3fc6-4efd-b24f-cba5af134a74",
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
  "content_id": "32c037fb-8db1-4cb4-b5d5-8716c7ec9e01",
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
  "content_id": "33be49ab-c10b-49ea-819b-84120362f058",
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
  "content_id": "cac5d4c0-1ae6-4a92-a978-463d045b7a37",
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
  "content_id": "24ef02b0-851d-4124-af71-b8247c503425",
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
  "content_id": "fe2c9178-e286-4070-b6df-b6c03f21ba86",
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
  "content_id": "01378724-988c-42fb-9fd4-a5566c2b7ef5",
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
  "content_id": "804e078f-b7c0-41b5-9084-d7f240b44ab6",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "d9dbdcd0-0d91-4a7c-b5d2-7e7edd06b672",
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
  "content_id": "e0c2426a-7ef0-4bfc-a9da-fa59a2fd7e73",
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
  "content_id": "072a53e2-f5d6-4452-9dab-68d4e3f33c4b",
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
  "content_id": "9cfe335b-a178-423f-b880-509b0302c3e1",
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
  "content_id": "f7580f2d-8016-41cf-970d-39447b6e9e6d",
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
