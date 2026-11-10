"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

import uuid

import audit

# NOTE: these ten pieces were drafted by an AI assistant as stand-ins, at the
# instructor's request, for a demonstration of the material. They are NOT the
# student's own writing, so criterion 1 results from this file are not a real
# measurement. Students must replace them with their own paragraphs.
OWN_WRITING = [
    "I missed the bus again this morning, which is becoming a bad habit. Ran the last block with my bag banging "
    "against my hip and still watched the doors close. Got to work twenty minutes late and said the trains were "
    "bad. Nobody checked. I felt oddly guilty about it all day.",
    "My grandmother kept her recipes on index cards stained with butter and, I think, some regret. The one for "
    "apple cake just says 'enough sugar, ask Dolores'. Dolores died in 1994. So that's the cake I make, and it "
    "never comes out right, and I keep making it anyway.",
    "Honestly the best part of the trip was the wrong turn. We were meant to be at the lake by noon, but Sam "
    "swore he knew a shortcut, and we ended up eating peaches at a gas station in the middle of nowhere while a "
    "man explained his theory about owls. Zero regrets.",
    "The landlord finally fixed the heater, three weeks and eleven emails later. It now makes a noise like a "
    "small animal being gently strangled, but it works. I wrote him a thank-you note. Sarcasm, mostly. A little "
    "sincerity slipped in, which annoyed me.",
    "I've been learning to bake bread and so far I've made four bricks and one loaf that was actually fine. "
    "The trick, apparently, is patience, which I don't have. My starter is named Gerald. Gerald is doing better "
    "than I am, frankly.",
    "Dear Priya, sorry this is late. The week got away from me and then the weekend did too. About the "
    "deadline: can we push it to Friday? I'll have the draft done by Wednesday, and I'd rather give you "
    "something decent than something on time.",
    "Rain all day. I watched a pigeon try to share a doorway with a man in a suit, and neither of them gave an "
    "inch. I don't know why that was the highlight of my Tuesday, but it was. I bought soup after. Good soup.",
    "When my brother was nine he decided he could fly if he ran fast enough off the garden wall. He couldn't. "
    "He broke his wrist and was proud for months, because the cast got signed by the whole class. That's the "
    "story he tells at every wedding.",
    "Two things I learned from the move: I own too many mugs, and nobody ever comes back for the box marked "
    "'misc'. Mine had a stapler, a left glove, and a photo of someone I can't place. I kept the photo. Threw out "
    "the glove, then felt bad.",
    "The library closes at eight, but the guy at the desk lets people stay a bit longer if you look desperate. "
    "I looked desperate on Thursday. Finished the chapter, left at 8:40, and he nodded at me like we'd pulled "
    "off a heist together.",
]

AI_WRITING = [
    "Effective communication is a cornerstone of success in the modern workplace. By fostering open dialogue, "
    "organizations can enhance collaboration, improve productivity, and build a culture of trust. Furthermore, "
    "clear communication helps teams navigate challenges and achieve their strategic objectives.",
    "Artificial intelligence has the potential to transform numerous industries by automating routine tasks and "
    "providing valuable insights. Moreover, it enables organizations to make data-driven decisions, optimize "
    "operations, and deliver more personalized experiences to customers across diverse sectors.",
    "In today's fast-paced world, maintaining a healthy work-life balance is essential for overall well-being. "
    "By prioritizing self-care, setting clear boundaries, and managing time effectively, individuals can reduce "
    "stress and enhance their productivity and long-term satisfaction.",
    "Climate change represents one of the most significant challenges facing humanity today. It is important to "
    "note that addressing this issue requires coordinated action from governments, businesses, and individuals. "
    "Ultimately, sustainable practices are crucial for ensuring a prosperous future for generations to come.",
    "Renewable energy sources, such as solar and wind power, offer a sustainable alternative to fossil fuels. "
    "These technologies not only reduce greenhouse gas emissions but also create economic opportunities. "
    "Additionally, advancements in energy storage continue to improve their reliability and overall efficiency.",
]

PLAIN_HUMAN = (
    "I went to the store yesterday to buy some groceries. The prices were higher than I expected, so I only "
    "bought the essentials. I got milk, bread, and eggs. It was a pretty normal trip overall. Then I went home "
    "and made dinner."
)


def _run_appeals(url, requests, trial):
    """Criterion 4: five submissions, each appealed. Returns one result per appeal."""
    results = []
    for i, text in enumerate(OWN_WRITING[:5], 1):
        creator = f"eval_appeal_t{trial}_{i}_{uuid.uuid4().hex[:6]}"
        sub = requests.post(f"{url}/submit", json={"text": text, "creator_id": creator}, timeout=90)
        cid = sub.json().get("content_id")
        app_resp = requests.post(f"{url}/appeal", json={"content_id": cid, "reasoning": "I wrote this myself."},
                                 timeout=30)
        entries = audit.entries_for(cid) if cid else []
        decisions = [e for e in entries if "event" not in e]
        appeals = [e for e in entries if e.get("event") == "appeal" and e.get("status") == "under_review"]
        ok = (app_resp.status_code == 200 and app_resp.json().get("status") == "under_review"
              and len(decisions) == 1 and decisions[0].get("status") == "decided" and len(appeals) == 1)
        results.append({"passed": ok, "submit_status": sub.status_code, "appeal_status": app_resp.status_code,
                        "appeal_body": app_resp.json(), "decision_entries": len(decisions),
                        "appeal_entries": len(appeals), "content_id": cid})
    return results


def _run_bad_input(url, requests, trial):
    """Criterion 5: 400/413, no scored decision, and a rejection in the audit log."""
    bodies = {
        "missing_text": lambda c: {"creator_id": c},
        "empty_text": lambda c: {"text": "", "creator_id": c},
        "whitespace_text": lambda c: {"text": "   \n\t ", "creator_id": c},
        "null_text": lambda c: {"text": None, "creator_id": c},
        "over_50000_chars": lambda c: {"text": "word " * 10001, "creator_id": c},
    }
    results = []
    for kind, make in bodies.items():
        creator = f"eval_bad_{kind}_t{trial}_{uuid.uuid4().hex[:6]}"
        resp = requests.post(f"{url}/submit", json=make(creator), timeout=90)
        entries = [e for e in audit.read_entries() if e.get("creator_id") == creator]
        decisions = [e for e in entries if "event" not in e]
        rejections = [e for e in entries if e.get("event") == "rejected"]
        ok = resp.status_code in (400, 413) and not decisions and len(rejections) >= 1
        results.append({"passed": ok, "kind": kind, "status": resp.status_code,
                        "decision_entries": len(decisions), "rejection_entries": len(rejections),
                        "body": resp.json() if resp.content else None})
    return results


SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": OWN_WRITING,
    },
    {
        "name": "score spread AI",
        "criterion": 2,
        # Compared against the "my own writing" scores from the same trial.
        "texts": AI_WRITING,
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            AI_WRITING[0],
            AI_WRITING[3],
            PLAIN_HUMAN,
            "I went to the park on Sunday. The weather was nice. I walked for an hour and then sat on a bench. "
            "It was a quiet day, and I liked that.",
            OWN_WRITING[3],
            OWN_WRITING[1],
        ],
    },
    {
        "name": "valid appeals",
        "criterion": 4,
        "run": _run_appeals,
    },
    {
        "name": "bad input",
        "criterion": 5,
        "run": _run_bad_input,
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if scenario.get("run"):
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
