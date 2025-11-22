# /import_queue

Staging area for raw or semi-processed content waiting to be converted into `/data`.

Examples:
- `npcs/valaria_eldenhold/*.csv`    – NPC exports from Notion or sessions
- `locations/*.csv`                 – Location exports
- `stories/*.md` or `.txt`         – Draft stories before JSON conversion
- `sessions/*.txt`                 – WhisperX transcripts or merged session logs

Automation scripts should:
1. Read from `/import_queue/...`
2. Generate structured JSON into `/data/...`
3. Optionally generate Markdown into `/site/pages/...`
4. Leave a trail of what was processed (either here or under `/ai/logs`).
