# Phase Status

> Update this file at the end of every work session, in any tool. This is how
> context survives across tools and across time. See AGENTS.md §6.

**Current phase: 0 — Foundational setup**

---

## Phase 0 — Docs + repo scaffolding
**Status:** In progress

- [x] ARCHITECTURE.md drafted
- [x] AGENTS.md drafted
- [x] PHASE_STATUS.md created (this file)
- [x] DECISIONS.md created
- [ ] API_CONTRACT.md created (can stay empty/skeleton until Phase 1 backend work starts)
- [x] GitHub repo created and these docs committed
- [ ] Stack tooling installed locally (Python + FastAPI scaffold, MediaPipe, Next.js scaffold)
- [ ] Supabase project created (free tier)

**Exit criteria:** all boxes above checked, repo exists with docs committed.

---

## Phase 1 — Squat form checker (uploaded video)
**Status:** Not started

- [ ] Define test set of squat videos (good form + 2-3 common errors) — see Decisions log once defined
- [ ] MediaPipe pose extraction working on a single uploaded video
- [ ] Rep-counting logic
- [ ] Squat rule engine (depth, knee valgus, forward lean — finalize exact rules in DECISIONS.md)
- [ ] Plain-language feedback generation (Claude API call)
- [ ] Manual validation against test set
- [ ] Phase 1 exit review with user before starting Phase 2

**Exit criteria:** defined in ARCHITECTURE.md §6 — system correctly flags good/bad form
on our test set, validated by hand.

---

## Phase 2 — Live webcam mode
**Status:** Not started — do not begin until Phase 1 is marked Done above.

---

## Phase 3 — Web app shell
**Status:** Not started.

---

## Phase 4 — Gym CCTV integration
**Status:** Not started.

---

## Phase 5 — Mobile app
**Status:** Not started.

---

## Phase 6+ — Trainer dashboards, gym analytics, workout recommendations
**Status:** Not started / not yet scoped.
