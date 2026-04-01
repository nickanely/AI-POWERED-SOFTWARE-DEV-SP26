# Architecture Diagram Checklist

Before committing your diagram, verify every item below. If any item is unchecked, the diagram is incomplete.

---

## Five Required Elements

- [ ] **Frontend** is shown — label it with what it actually is (browser, React app, Gradio UI, CLI)
- [ ] **Backend** is shown — label it with what it actually is (FastAPI, Flask, Next.js, serverless)
- [ ] **AI model** is shown — label it with the specific model name (Gemini 3 Flash, DALL-E 3, Whisper)
- [ ] **Storage** is shown — label it with the specific technology (Postgres, SQLite, FAISS, Supabase)
- [ ] **Arrows** show data direction between every connected pair of components

## Correctness

- [ ] Arrows have direction (not just lines)
- [ ] No component floats without a connection
- [ ] The diagram matches the technology stack table in Section 4 of DESIGN-REVIEW.md
- [ ] OpenRouter is shown if you route through it (not just "AI model")

## File

- [ ] Saved as `architecture-diagram.png` (or `.jpg`, `.svg`, `.pdf`)
- [ ] Committed to `design-review/` in team repo
- [ ] Readable when opened at normal screen size — not too small, not blurry
- [ ] Referenced in DESIGN-REVIEW.md Section 4

---

Once all items are checked, commit and move to the data flow.
