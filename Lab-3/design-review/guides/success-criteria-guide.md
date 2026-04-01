# Guide: Writing Measurable Success Criteria

Success criteria tell you — and your grader — whether your product is working. They must be testable. If you cannot run a test tomorrow and get a number, your criterion is not measurable.

---

## The Formula

Every criterion follows this structure:

**[What you measure] achieves [target number] when tested [how you measure it].**

All three parts are required. Missing any one of them makes the criterion untestable.

---

## Common Wrong Patterns and How to Fix Them

**Wrong:** "Our app will be accurate."
**Why it fails:** No number, no measurement method.
**Fixed:** "Receipt field extraction achieves greater than 85% accuracy across our 20-item test set of receipt photos."

**Wrong:** "Users will find it easy to use."
**Why it fails:** Subjective, no measurement method.
**Fixed:** "A new user completes the core workflow (upload receipt, review extraction, confirm) in under 2 minutes on first attempt."

**Wrong:** "The AI will respond quickly."
**Why it fails:** No number.
**Fixed:** "95% of API responses return within 3 seconds under normal load."

**Wrong:** "We will handle errors gracefully."
**Why it fails:** No measurement.
**Fixed:** "Zero unhandled exceptions reach the user in a 30-minute session of normal usage."

---

## Two Criteria You Can Almost Always Write

These apply to most capstone projects regardless of domain:

**Quality criterion:** Measures whether your AI feature produces correct or useful outputs.
Example format: "[Feature name] achieves [X%] [accuracy / precision / recall / correct classification] on a manually verified test set of [N] items."

**Reliability criterion:** Measures whether your system handles failures cleanly.
Example format: "When the AI returns a confidence score below [threshold], the fallback UX triggers correctly in [X out of X] test cases."

---

## For Your Specific Domain

If your product is in one of these domains, here are starting points:

**EdTech / tutoring:** "The system correctly identifies the error type in student work for [X]% of a 20-item annotated test set."

**Health / wellness:** "Calorie estimates are within [X]% of verified nutritional data for [N] standardised meal photos."

**Finance / expense:** "Invoice field extraction achieves [X]% accuracy (amount, date, vendor) across [N] test invoices spanning handwritten, printed, and photo formats."

**Creative tools:** "Generated assets meet the team's defined style guide criteria in [X] out of [N] blind evaluations."

**Accessibility / language:** "Translation accuracy rated 'acceptable' or above by a native speaker in [X]% of [N] test sentences."

---

## What the Grader Is Looking For

A 2-point score on this section requires:
- At least two criteria
- Each criterion has a target number
- Each criterion has a measurement method you could actually execute

A 1-point score gets awarded when criteria exist but lack numbers or measurement methods.
