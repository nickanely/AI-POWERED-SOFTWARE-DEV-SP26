# Guide: Data Governance

Six questions. Most teams can complete this in under 10 minutes if they answer directly.

---

## The Six Questions

**1. What user data does your app collect or process?**
List every type. Examples: uploaded photos, typed text, voice recordings, email address, name, document contents, location.

**2. Where is it stored?**
Name the specific service and the country where the servers are. Examples: "Supabase (EU region)", "local SQLite file on the user's machine", "not stored — processed and discarded", "Vercel blob storage (USA)".

**3. How long is it retained?**
Examples: "not retained — processed in memory and discarded immediately", "stored for 30 days then automatically deleted", "retained until the user deletes their account".

**4. Who has access to it?**
Examples: "only the user themselves (authentication required)", "the instructor for grading purposes", "the development team via the database dashboard".

**5. How can a user request deletion?**
Examples: "email us at [address]", "via the Delete Account button in settings", "we do not store data so deletion is not applicable".

**6. Does your app send user data to third-party AI APIs? Which ones?**
Examples: "yes — user-uploaded images are sent to OpenRouter / Google Gemini for vision analysis", "yes — user text is sent to OpenAI via OpenRouter for completion", "no — all processing is local".

---

## Common Cases

**If your app does not store any user data:** Answer question 1 ("we process X"), then for questions 2 and 3 write "not stored — processed in memory and discarded", and for question 5 write "not applicable — no data is retained".

**If your app uses OpenRouter:** For question 6, write "User inputs are sent to OpenRouter and then forwarded to [model provider]. OpenRouter's privacy policy governs their data handling."

**For voice or audio:** The syllabus specifically requires: "explicit consent, automatic deletion after processing". Your governance plan must include these two things.
