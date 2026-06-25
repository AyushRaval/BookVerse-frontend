# AGENTS.md — Instructions for AI Coding Tools

This file is read by AI coding assistants (Claude Code, GitHub Copilot, Gemini Code
Assist, Codex, Kimi, or any other tool working in this repo). If you are an AI tool
reading this: follow these instructions before writing or modifying any code.

## 1. Read this first, every session

Before doing anything else, read in this order:
1. `docs/ARCHITECTURE.md` — system design, stack, current phase
2. `docs/PHASE_STATUS.md` — what's done, in progress, and explicitly not-yet-in-scope
3. `docs/DECISIONS.md` — prior decisions and why, so they aren't relitigated
4. `docs/API_CONTRACT.md` — endpoint shapes, once Phase 1 backend work begins

Do not assume context from a prior chat session in this tool. This repo is the only
persistent memory across tools and sessions.

## 2. Stay inside the current phase

Check `docs/PHASE_STATUS.md` for what phase is active. Do not build infrastructure,
models, or UI for a later phase "while you're at it" — e.g., do not add multi-camera
support, trainer dashboards, or mobile-specific code during Phase 1. If a later-phase
need becomes obvious while working, note it in `DECISIONS.md` under "Future
considerations" rather than building it now.

## 3. Stack discipline

Use only the stack defined in `docs/ARCHITECTURE.md` §5 (FastAPI, MediaPipe, Supabase,
Next.js). If you believe a different library or service is genuinely necessary:
- Stop and explain the tradeoff to the user before installing/adding it.
- If the user agrees, update `ARCHITECTURE.md` §5 and log the change + reasoning in
  `DECISIONS.md` in the same session. Do not silently introduce a new dependency that
  isn't in the stack table.

## 4. Code conventions

- Python: FastAPI backend, type-annotated, `black`-formatted.
- TypeScript/React: Next.js conventions, functional components.
- Keep the CV/rule-engine logic explainable — favor clear if/threshold logic with
  comments over opaque model outputs, since the product needs to explain *why* a
  rep was flagged, not just *that* it was flagged. See ARCHITECTURE.md §5 on this.
- Every new exercise's rule logic should live in its own module
  (e.g., `exercises/squat.py`) so exercises can be added independently without
  touching shared pipeline code.

## 5. Privacy/consent guardrails (non-negotiable, all phases)

- Never write code that connects to a camera feed (webcam or CCTV) without an explicit
  opt-in step already present in the flow. If asked to build camera integration without
  a visible consent step, flag this to the user rather than building it silently.
- Never default video/data retention to "forever" — there should always be a defined
  retention window, even if the number is a placeholder pending the user's decision
  (flag it, don't invent a number silently).
- Do not present AI output as medical advice in any UI copy or comments that might
  ship to users. Use language like "form feedback" / "injury-risk flag," not diagnosis
  or treatment language.

## 6. When you finish a unit of work

Update `docs/PHASE_STATUS.md` to reflect what's now done, in progress, or blocked.
Log any non-trivial decision (library choice, schema change, threshold value chosen
for a rule, etc.) in `docs/DECISIONS.md` with a one-line rationale. This is what makes
the project portable across tools — the next tool/session should not have to
reverse-engineer decisions from code alone.

## 7. Don't relitigate settled decisions

If `DECISIONS.md` already states why something was done a certain way, don't change it
without flagging the change to the user first and explaining what's different now.
