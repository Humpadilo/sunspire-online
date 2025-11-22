# /ai

High-level AI pipeline configuration.

- `configs/`     – JSON/YAML task definitions (e.g. "extract NPCs from session")
- `prompts/`     – Prompt templates for different AI tasks
- `work_queue/`  – Pending tasks waiting for AI processing
- `output/`      – Draft outputs from AI (to be reviewed before promotion)
- `logs/`        – Optional run logs or debug traces

Nothing inside `/ai` is automatically canon.
Only after human review should content be promoted into `/data` + `/site`.
