# Safety Threats Template

Fill in every row. For threats that do not apply, write "N/A" and one sentence explaining why. A blank cell scores zero. An "N/A" with a reason scores full marks for that row.

---

## Threat Table

Copy this table into Section 7 of DESIGN-REVIEW.md and fill it in.

| Threat | Relevant to our product? | Our mitigation |
|---|---|---|
| **Prompt injection** — user input overrides system instructions | Yes / No / Partial | |
| **Hallucination in high-stakes output** — model returns confident wrong answers in a consequential context | Yes / No / Partial | |
| **Bias affecting specific user groups** — systematically different output quality by language, name, or demographic | Yes / No / Partial | |
| **Content policy violation** — user-submitted prompts trigger content filters | Yes / No / Partial | |
| **Privacy violation** — user data sent to third-party APIs without adequate disclosure | Yes / No / Partial | |
| **Data exfiltration** — malicious prompt causes model to reveal other users' data or internal configuration | Yes / No / Partial | |

---

## Top Risk

After filling the table, name the single threat you are most concerned about for your specific product and why:

```
Our biggest safety concern is [threat name] because [specific reason related to our product and users].
```

---

## Writing Good Mitigations

**Weak:** "We will validate inputs."
**Strong:** "All user text inserted into prompts is stripped of special characters and length-limited to 500 characters before insertion. The system prompt is in a separate message from user content so it cannot be overwritten."

**Weak:** "We will handle errors."
**Strong:** "Any output containing medical-sounding claims is appended with 'This is not medical advice — verify with a qualified professional' before display."

One specific sentence beats a vague paragraph every time.
