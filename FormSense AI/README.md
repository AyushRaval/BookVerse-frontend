# FormSense AI (placeholder name)

AI-powered fitness form/posture analysis platform. Web app first, mobile later.
Target market: India, primarily Ahmedabad.

## Start here

If you're a person or an AI coding tool picking this up for the first time, read in
this order:

1. `docs/ARCHITECTURE.md` — what this is, the stack, the phased roadmap
2. `docs/AGENTS.md` — rules for AI coding tools working in this repo
3. `docs/PHASE_STATUS.md` — what's currently in progress
4. `docs/DECISIONS.md` — why things are the way they are

**We are currently in Phase 0** (foundational setup — no feature code yet).

## Why this structure exists

This project is built across multiple AI coding tools (Claude Code, GitHub Copilot,
Gemini, Codex, etc.) on purpose. The `/docs` folder — not any individual tool's chat
history — is the single source of truth, so context survives switching tools. Every
tool is instructed (via `AGENTS.md`) to read `/docs` before writing code, and to log
decisions back into `/docs` after finishing work.
