# Decisions Log

> One entry per non-trivial decision. Newest at the top. Keep entries short —
> what was decided and why, not a transcript of the discussion.

---

### 2026-06-25 — Project placeholder name: "FormSense AI"
Real name not yet chosen. Using this as a placeholder across docs/code/packages.
**Action when renamed:** search/replace "FormSense AI" repo-wide, including package
names, and re-check this log for references.

### 2026-06-25 — Database/auth/storage: Supabase
Chosen over self-hosted Postgres for Phase 1–3. Reasoning: one free-tier platform
covers Postgres + auth + file storage, reducing infra glue at a stage where that
complexity isn't earning its cost. Revisit only if/when scale or specific feature
needs (e.g., complex row-level security beyond Supabase's model) require it —
log the reasoning here if we ever migrate.

### 2026-06-25 — Backend stack: Python + FastAPI
Chosen for native fit with MediaPipe/CV libraries and strong support across AI coding
tools (Claude Code, Copilot, Gemini, Codex all handle this stack well), which matters
for the multi-tool workflow described in ARCHITECTURE.md.

### 2026-06-25 — Pose estimation: MediaPipe Pose
Chosen over alternatives (e.g., OpenPose, MoveNet) because it's free with no per-call
API cost, runs without a GPU requirement at small scale, and has mature
Python bindings. Revisit if accuracy on the Phase 1 test set proves insufficient.

### 2026-06-25 — Form analysis approach: rule engine, not black-box ML
Decided to build exercise-specific rule logic on top of MediaPipe keypoints (joint
angles, thresholds) rather than training a separate classifier for "good/bad form."
Reasoning: explainability — the product needs to tell a user *why* a rep was flagged,
which a rule engine supports directly and a black-box classifier does not, without
significant additional interpretability work. Can revisit per-exercise if rule-based
accuracy plateaus.

### 2026-06-25 — Feedback text generation: Claude API (small/cheap tier)
Used only to turn structured rule-engine output into plain-language sentences — not
used for the core form-detection logic itself. Low token count per call keeps this
cheap regardless of usage volume.

### 2026-06-25 — First exercise to validate: Squat
Chosen as the Phase 1 validation exercise. Squat has well-documented common form
errors (knee valgus, insufficient depth, excessive forward lean, heel lift) that map
cleanly to measurable joint angles, making it a good first test of the rule-engine
approach before generalizing to other exercises.

### 2026-06-25 — Phase ordering: uploaded video → live webcam → CCTV
CCTV deliberately sequenced last. Reasoning: (1) technically hardest — multi-person
tracking, camera calibration, RTSP/stream ingestion at scale; (2) different consent
category — gym CCTV monitoring of members is a materially different privacy posture
than a user voluntarily uploading their own video, and we want the core CV engine
proven before taking on that complexity. See ARCHITECTURE.md §7.

### 2026-06-25 — Target market: India, primarily Ahmedabad
Initial focus market. Product designed so consent/retention rules can be tightened
per-jurisdiction later (e.g., for GDPR/BIPA markets) via configuration rather than a
rewrite, even though current target market has lighter regulatory strictness.

---

## Open / pending decisions (not yet finalized)

- **Video retention window:** exact duration not yet decided. Must be decided before
  Phase 1 ships to any real (non-test) user. Do not default to indefinite retention.
- **Phase 1 test set:** specific squat videos (good form + named error types) not yet
  assembled. Needed before rule-engine validation can begin.
- **Final product name:** placeholder "FormSense AI" in use; check trademark/domain
  availability before finalizing.
