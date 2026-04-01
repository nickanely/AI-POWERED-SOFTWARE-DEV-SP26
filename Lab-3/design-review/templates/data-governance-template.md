# Data Governance Template

Six questions. Answer each one directly. Copy the completed table into Section 8 of DESIGN-REVIEW.md.

---

## Governance Table

| Question | Your answer |
|---|---|
| **What user data does your app collect or process?** List every type — uploaded files, typed text, voice recordings, email, name, location, document contents. | |
| **Where is it stored?** Name the specific service and the country. If nothing is stored, write "not stored — processed in memory and discarded." | |
| **How long is it retained?** Give a specific period or condition — "30 days", "until account deletion", "not retained — discarded after processing". | |
| **Who has access to it?** — "only the authenticated user", "the development team via the database dashboard", "the instructor for grading purposes". | |
| **How can a user request deletion?** — "via the Delete Account button", "email us at [address]", "not applicable — no data is retained". | |
| **Does your app send user data to third-party AI APIs? Which ones?** Name every external API that receives any user input. | |

---

## Special Cases

**If you use voice or audio:** The syllabus requires "explicit consent, automatic deletion after processing." Your answers to questions 3 and 5 must address both of these.

**If you use OpenRouter:** For question 6, write: "User inputs are forwarded to [model provider] via OpenRouter. OpenRouter's data handling policy applies to data in transit."

**If you are uncertain:** Make a decision, write it down, and note it is provisional. "We have not decided yet" is not an acceptable answer.
