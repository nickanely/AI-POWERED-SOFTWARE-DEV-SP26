# Guide: Architecture Diagram

Your Lab 2 proposal had a prose description of the technical architecture. That is not enough for the Design Review. You need a visual diagram.

---

## What Must Be In the Diagram

Five elements. Every element must be present. The grader checks these explicitly.

1. **Frontend** — what the user interacts with (browser interface, mobile app, CLI, Gradio UI)
2. **Backend** — your server or API (FastAPI, Flask, Next.js API route, serverless function)
3. **AI model** — name the specific model (e.g., "Gemini 3 Flash", "DALL-E 3"). Do not write "AI" or "LLM".
4. **Storage** — where data lives (Postgres, SQLite, Supabase, FAISS, local files)
5. **Arrows** — showing which direction data flows between every pair of connected components

If your architecture has more components (OpenRouter as router, a queue, a vector store), include them. The five above are the minimum.

---

## Acceptable Formats

Any of these work. Pick the fastest one for your team right now.

**Hand-drawn and photographed:** Draw on paper or a whiteboard, photograph it, commit the photo. This takes 5 minutes and scores the same as a polished diagram.

**Excalidraw:** Free, browser-based, no account needed. excalidraw.com. Export as PNG.

**draw.io:** browser-based. drawio.com. Export as PNG.

**Miro:** If your team already uses it.

**Any drawing tool:** If it produces a PNG you can commit, it works.

---

## What an Architecture Diagram Is Not

It is not a flowchart of user actions. It is not a data flow trace (that is Section 5). It is not a list of technologies in a table. It is a visual showing the components of your system and how they are connected.

---

## Committing the Diagram

Save as `architecture-diagram.png` (or `.jpg`, `.svg`, `.pdf`). Commit it to `design-review/` in your team repo. Reference it in DESIGN-REVIEW.md Section 4:

```
See: design-review/architecture-diagram.png
```

---

## Quick Checklist Before Committing

Use `templates/architecture-template.md` to verify your diagram has everything before committing.
