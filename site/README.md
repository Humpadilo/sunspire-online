# /site

Public website content.

- `assets/` – Images, CSS, JS, fonts, etc.
- `pages/`  – Markdown/HTML pages grouped by type:
  - `locations/`
  - `npcs/`
  - `factions/`
  - `stories/`
  - `sessions/`
- `map/`    – Map-related HTML/JS (player map build, not DM-only overlays)

JSON in `/data` should link to one or more pages in `/site/pages/...`
for human-readable lore.
