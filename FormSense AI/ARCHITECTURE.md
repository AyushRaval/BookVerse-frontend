# FormSense AI — Architecture

> **Placeholder name.** Replace "FormSense AI" project-wide once a final name is chosen
> (check trademark + domain availability first). Search/replace this string across
> `/docs`, `README.md`, and package names when renamed.

**Status:** Phase 0 — foundational setup, no feature code yet.
**Last updated:** 2026-06-25

---

## 1. Purpose

An AI-powered platform that analyzes exercise form, posture, and movement quality from
video, gives users personalized feedback, and (in later phases) connects to gym cameras
for real-time, opt-in monitoring.

**Initial target market:** India, primarily Ahmedabad. Built so consent/data-retention
rules can tighten per-jurisdiction later without a rewrite (see §7).

---

## 2. Build Philosophy

- **Step-by-step, not fast.** Each phase is fully validated before the next begins.
  Do not start Phase N+1 work until Phase N is marked Done in `PHASE_STATUS.md`.
- **One source of truth.** This repo's `/docs` folder is the spec. Any AI coding tool
  (Claude Code, Copilot, Gemini, Codex, etc.) must read `/docs` before writing code.
  Chat history inside any single tool is not the source of truth — this repo is.
- **Boring, well-supported stack.** Every technology chosen here was chosen because
  multiple AI coding tools understand it well and it has a free or cheap tier at small
  scale. Novelty is a cost, not a benefit, at this stage.

---

## 3. Phased Roadmap

| Phase | Goal | Exit criteria |
|---|---|---|
| **0** | Docs + repo scaffolding (this phase) | `/docs` complete, repo created, stack confirmed |
| **1** | CV core: squat form-check on **uploaded video** | Given a squat video, system correctly flags good/bad form on a test set we define |
| **2** | Live webcam mode | Same accuracy as Phase 1, running on a live stream with acceptable latency |
| **3** | Web app shell | Auth, upload UI, results dashboard, basic progress history |
| **4** | Gym CCTV integration | Multi-person tracking, opt-in consent flow, per-gym onboarding |
| **5** | Mobile app | Same backend API, React Native or Flutter client |
| **6+** | Trainer dashboards, gym analytics, AI workout recommendations | Defined when we get there |

We are currently scoping **Phase 1**. Do not build Phase 2+ infrastructure early
"just in case" — it adds complexity before we know Phase 1's CV approach actually works.

---

## 4. System Overview (target end-state)

```
                       ┌─────────────────────┐
                       │   Next.js Frontend   │
                       │  (web, later mobile)  │
                       └──────────┬───────────┘
                                  │ HTTPS / REST
                       ┌──────────▼───────────┐
                       │   FastAPI Backend     │
                       │  (auth, CRUD, jobs)   │
                       └──────────┬───────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
   ┌──────────▼─────────┐ ┌───────▼──────┐  ┌─────────▼─────────┐
   │  Supabase Postgres   │ │ Supabase     │  │  CV Inference       │
   │  (users, workouts,   │ │ Storage      │  │  Service (Python)   │
   │  sessions, scores)   │ │ (video files) │  │  MediaPipe + rules  │
   └───────────────────────┘ └──────────────┘  └─────────────────────┘
```

In Phase 1, the "CV Inference Service" can live inside the FastAPI backend as a module —
do not split it into a separate microservice until latency or scaling actually requires it.

---

## 5. Tech Stack (decided)

| Layer | Choice | Why |
|---|---|---|
| Backend | Python + FastAPI | Native fit with CV/ML libraries; async support for job handling |
| Pose estimation | MediaPipe Pose (Google) | Free, runs locally (no per-call API cost), good accuracy for single-person full-body |
| Form analysis | Custom rule engine on top of MediaPipe keypoints | Exercise-specific joint-angle/posture rules; not a generic ML black box — needs to be explainable to users |
| Feedback text generation | Claude API (small/cheap model tier) | Turns structured rule-engine output into plain-language feedback; low token count per call |
| Database | Supabase (Postgres) | Free tier, includes auth + storage, avoids stitching 3 separate services together |
| File storage | Supabase Storage | Video uploads and processed clips |
| Auth | Supabase Auth | Free, integrates directly with the DB |
| Frontend | Next.js (React) | Strong AI-tool support, easy path to consistent design system |
| Job queue (Phase 1: optional) | Start synchronous; add Redis + worker queue only if video processing time requires async by Phase 3 | Don't add infra before it's needed |

**Do not introduce a different database, auth provider, or pose library without updating
this table and logging why in `DECISIONS.md`.**

---

## 6. Phase 1 Detail — Squat Form Checker (Uploaded Video)

**Scope:** user uploads a video of themselves squatting → system returns:
- Rep count
- Per-rep form flags (e.g., knees caving in, insufficient depth, excessive forward lean)
- A plain-language summary

**Out of scope for Phase 1:** live webcam, multiple exercises, multiple people in frame,
trainer dashboards, progress history over time. One exercise, one person, one video, in
and out.

**Validation approach:** before writing the rule engine, we define a small test set of
squat videos (good form + specific common errors) and check the system's output against
it by hand. Accuracy on this test set is the Phase 1 exit criterion — see `DECISIONS.md`
for the actual test set once defined.

---

## 7. Privacy & Consent (carried through every phase)

- No gym or user is connected to camera-based monitoring without explicit opt-in.
  Uploaded video (Phase 1–3) is submitted voluntarily by the user, which is a materially
  different consent posture than CCTV (Phase 4) — do not conflate the two in code or UX.
- Data retention: define an explicit retention window for video files (not indefinite by
  default). To be finalized before Phase 1 ships to any real user — track in
  `DECISIONS.md`.
- Users must be able to request deletion of their data (videos + derived analysis).
- Aligns with India's DPDP Act 2023 (biometric-adjacent data) from day one, even though
  enforcement/strictness is currently lighter in our initial market. Designed so
  stricter regimes (GDPR, BIPA) can be supported later via configuration, not rewrite.
- The product gives form/injury-risk feedback, not medical advice. This must be visible
  in the UI (not just buried in ToS) before a user sees their first result.

---

## 8. What Each AI Coding Tool Should Do

See `AGENTS.md` for tool-facing instructions. Summary: read `/docs` first, check
`PHASE_STATUS.md` for what's currently in scope, log any architectural decision in
`DECISIONS.md`, and do not build ahead of the current phase.
