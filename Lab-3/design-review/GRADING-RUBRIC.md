# Design Review Grading Rubric

**10 points total | Due Thursday 2 April 2026 at 23:59**

---

## Required Team Repo Tree

Graders navigate your repo directly. Files in the wrong location score zero for that section.

```
[your-project-name]/
├── README.md
├── TEAM-CONTRACT.md                   ← Must be in repo root, not inside docs/
├── .gitignore                         ← .env must be excluded
├── .env.example
├── AGENTS.md                          ← Optional
│
├── frontend/                          ← Scaffold from Lab 2 Builder Sprint
│   └── [scaffold files]
│
├── backend/
│   └── [backend files]
│
├── docs/
│   └── design-review/                 ← Design Review files go here
│       ├── DESIGN-REVIEW.md           ← No [fill in] remaining
│       └── architecture-diagram.png   ← Readable visual
│
└── tests/
```

**Common mistakes that cost marks:**
- `DESIGN-REVIEW.md` placed at repo root instead of `docs/design-review/`
- `TEAM-CONTRACT.md` placed inside `docs/` instead of repo root
- Architecture diagram not committed — prose description does not earn the diagram point
- `.env` committed — automatic deduction on Criterion 4

---

## Criterion 1 — Clarity and Scope (2 points)

Covers Sections 1, 2, and 3 of DESIGN-REVIEW.md.

| Score | What it looks like |
|---|---|
| **2.0** | Problem names a specific user, specific pain, specific consequence. Success criteria have target numbers and measurement methods. Product scope is realistic for 15 weeks. |
| **1.5** | Problem is specific but success criteria lack numbers, or scope is slightly aspirational. |
| **1.0** | Problem is generic. Success criteria are qualitative ("will be accurate", "users will like it"). |
| **0.5** | Problem statement is vague. No success criteria present. |
| **0** | Section missing or entirely placeholder. |

**The line between 1.0 and 2.0:** The number. "Our extraction will be accurate" is 1.0. "Our extraction achieves greater than 85% field accuracy on a 20-item test set" is 2.0.

---

## Criterion 2 — Technical Depth (3 points)

Covers Sections 4 and 5 of DESIGN-REVIEW.md.

| Score | What it looks like |
|---|---|
| **3.0** | `architecture-diagram.png` committed in `docs/design-review/` showing all five elements (frontend, backend, named AI model, storage, arrows). Data flow traces a complete user action through every layer. Technology stack table fully completed. |
| **2.0** | Diagram exists but is missing one or two elements. Data flow present but incomplete. |
| **1.0** | Architecture described in prose only — no diagram file. Data flow not attempted. |
| **0** | Architecture section missing entirely. |

**The five required diagram elements:**
1. Frontend — label what it actually is (browser, React app, Gradio UI, CLI)
2. Backend — label what it actually is (FastAPI, Flask, Next.js, serverless)
3. AI model — named specifically (Gemini 3 Flash, DALL-E 3 — not just "AI" or "LLM")
4. Storage — named specifically (Postgres, SQLite, Supabase, FAISS, local files)
5. Arrows — showing direction of data flow between all connected components

A photo of a whiteboard sketch committed as `.png` earns the diagram point. Prose does not, regardless of quality.

---

## Criterion 3 — Reliability and Safety (3 points)

Covers Sections 7 and 8 of DESIGN-REVIEW.md.

| Score | What it looks like |
|---|---|
| **3.0** | At least 3 threats named with specific one-sentence mitigations. Fallback UX describes what the user sees (not error handling code). Data governance answers all 6 questions. |
| **2.0** | Threats present but mitigations vague. Fallback UX exists but framed as code logic. Data governance at least 3 questions answered. |
| **1.0** | One or two threats mentioned. No fallback UX. Fewer than 3 data governance answers. |
| **0** | Section missing or entirely placeholder. |

**Fallback UX — the difference between 2.0 and 3.0:**
- 2.0: "We will catch API errors and display an error message."
- 3.0: "The user sees the fields highlighted in amber with the label 'Please check these values'. A manual entry option appears below. The application never shows the word 'error' on screen."

The 3.0 answer describes the user experience. The 2.0 answer describes what the developer wrote.

---

## Criterion 4 — UX and Communication (2 points)

Covers the document as a whole, the team contract, and the repo structure.

| Score | What it looks like |
|---|---|
| **2.0** | `DESIGN-REVIEW.md` complete — no `[fill in]` remaining. `TEAM-CONTRACT.md` in repo root with all member names. Repo tree matches required structure. `README.md` updated. |
| **1.5** | Document mostly complete with minor gaps in non-critical sections. Contract exists. |
| **1.0** | Multiple sections have placeholder text. Contract missing or unsigned. |
| **0.5** | Document fragmentary. Repo structure unrecognisable. |
| **0** | Not submitted, or Google Form not completed. |

---

## Late Policy

| Hours late | Maximum score |
|---|---|
| On time | 10 |
| Up to 24 hours | 9 |
| 24 – 48 hours | 8 |
| 48 – 72 hours | 7 |
| Over 72 hours | Contact instructor before submitting |
