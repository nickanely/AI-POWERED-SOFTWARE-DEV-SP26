# Example: Measurable Success Criteria

The examples below are for a fictional expense receipt processing app. Use them as a pattern — adapt the structure for your own product domain.

---

## Weak Criteria (these score 0.5 or below)

| Criterion | Why it fails |
|---|---|
| "Our app will be accurate." | No number. No measurement method. Untestable. |
| "Users will find it easy to use." | Subjective. No measurement method. |
| "The AI will respond quickly." | No number. "Quickly" is undefined. |
| "We will handle errors gracefully." | No number. Not a success criterion — it is a design intention. |
| "The extraction will work well for most receipts." | "Most" is undefined. "Work well" is undefined. |

---

## Strong Criteria (these score 2.0)

**Criterion 1 — Extraction quality:**

> Receipt field extraction (amount, date, vendor) achieves greater than 85% accuracy across a manually verified test set of 20 receipt photos spanning printed thermal, handwritten, and phone-camera formats.

What makes this strong: specific fields named, specific number (85%), specific measurement method (manually verified test set), specific test set description (20 items, three formats).

**Criterion 2 — Fallback reliability:**

> When the model returns a field with confidence below 0.80, the amber highlight and manual entry prompt appear correctly in 100% of tested cases across 10 low-confidence scenario replays.

What makes this strong: specific threshold (0.80), specific expected behaviour (amber highlight + prompt), specific test count (10), completely testable right now.

**Criterion 3 — Latency:**

> 90% of receipt analysis calls complete within 4 seconds end-to-end (from button click to result display) in a testing environment with a standard home internet connection.

What makes this strong: specific percentile (90th), specific number (4 seconds), specific measurement point (button click to display), specific test condition (home internet).

---

## Template for Your Own Criteria

Use this sentence structure:

> [Feature name] achieves [target number] [unit of measurement] when tested [how you test it] across [how many / what kind of test cases].

Write one criterion about output quality and one about reliability or latency.

| | What you measure | Target number | How you measure it |
|---|---|---|---|
| **Criterion 1** | | | |
| **Criterion 2** | | | |
