"""
init_sunspire_public.py

One-time (and repeatable) scaffolding tool for D:\SunspireOnlinePublic.

- Creates the core folder structure
- Adds tiny README/.gitkeep files so humans & AIs know what goes where
- Safe to run multiple times (never overwrites existing files)
"""

from pathlib import Path
import textwrap

def main() -> None:
    # Repo root is one level up from /tools/
    root = Path(__file__).resolve().parents[1]

    # --- Core directories ---
    dirs = [
        # Canonical data (public JSON)
        "data",
        "data/locations",
        "data/npcs",
        "data/factions",
        "data/stories",
        "data/sessions",
        "data/items",

        # Public-facing site
        "site",
        "site/assets",
        "site/pages",
        "site/pages/locations",
        "site/pages/npcs",
        "site/pages/factions",
        "site/pages/stories",
        "site/pages/sessions",
        "site/map",

        # Documentation
        "docs",
        "docs/roadmap",

        # AI pipeline config (high-level, not actual models)
        "ai",
        "ai/configs",
        "ai/prompts",
        "ai/work_queue",
        "ai/output",
        "ai/logs",

        # Import queues for cleaned exports (from Notion, WhisperX, etc.)
        "import_queue",
        "import_queue/npcs",
        "import_queue/npcs/valaria_eldenhold",
        "import_queue/npcs/mireholm",
        "import_queue/npcs/sylvara",
        "import_queue/locations",
        "import_queue/stories",
        "import_queue/sessions",

        # Tools folder itself (in case someone moves this file)
        "tools",
    ]

    for d in dirs:
        path = root / d
        path.mkdir(parents=True, exist_ok=True)

    # --- Helper: write a file only if it doesn't exist ---
    def write_if_missing(rel_path: str, content: str) -> None:
        file_path = root / rel_path
        if file_path.exists():
            return
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")

    # --- Root README (only if you don't already have one) ---
    write_if_missing(
        "README.md",
        """
        # Sunspire Online (Public)

        This is the **public-facing** SunspireOnline repository.

        It contains:
        - `/data`      – Player-safe JSON data (locations, NPCs, factions, stories, sessions, items)
        - `/site`      – Markdown/HTML and assets for the public website
        - `/docs`      – Human-readable docs and roadmaps
        - `/ai`        – High-level AI configs, prompts, queues, and outputs
        - `/import_queue` – Staging area for cleaned exports waiting to be converted to JSON

        Authoritative DM-only content lives elsewhere (e.g. `D:\\Tracy`).
        This repo is the **readable, player-safe mirror**.
        """
    )

    # --- /data README ---
    write_if_missing(
        "data/README.md",
        """
        # /data

        Canonical JSON data for the **public** Sunspire world.

        Subfolders:
        - `locations/` – Cities, towns, dungeons, landmarks (player-safe fields only)
        - `npcs/`      – Public-facing NPC records (no secret twist lore)
        - `factions/`  – Factions and organizations
        - `stories/`   – One-shot vignettes and side stories
        - `sessions/`  – Session summaries (what actually happened in play)
        - `items/`     – Named items, artifacts, notable gear

        Each object is a single JSON file with a stable `id` and a small, consistent schema.
        """
    )

    # --- /site README ---
    write_if_missing(
        "site/README.md",
        """
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
        """
    )

    # --- /docs README ---
    write_if_missing(
        "docs/README.md",
        """
        # /docs

        Documentation for SunspireOnlinePublic.

        Suggested contents:
        - `roadmap/` – Pipeline and step-by-step plans (e.g. Sunspire_Online_Roadmap.md)
        - `data_model.md` – JSON schemas and examples
        - `world_hierarchy.md` – Nations, regions, cities, and their relationships
        - `command_reference.md` – Common commands for dev and automation

        This folder is for **humans and AIs** to understand how the repo is structured.
        """
    )

    # --- /docs/roadmap README ---
    write_if_missing(
        "docs/roadmap/README.md",
        """
        # /docs/roadmap

        Roadmap and step files for the Sunspire Online pipeline.

        Typical files:
        - `Sunspire_Online_Roadmap.md`
        - `CHATGPT_Sunspire_Online_Roadmap.md`
        - Any per-step breakdowns (Step 1–6)

        Treat this as the "project brain" for how data flows into `/data` and `/site`.
        """
    )

    # --- /ai README ---
    write_if_missing(
        "ai/README.md",
        """
        # /ai

        High-level AI pipeline configuration.

        - `configs/`     – JSON/YAML task definitions (e.g. "extract NPCs from session")
        - `prompts/`     – Prompt templates for different AI tasks
        - `work_queue/`  – Pending tasks waiting for AI processing
        - `output/`      – Draft outputs from AI (to be reviewed before promotion)
        - `logs/`        – Optional run logs or debug traces

        Nothing inside `/ai` is automatically canon.
        Only after human review should content be promoted into `/data` + `/site`.
        """
    )

    # --- /import_queue README ---
    write_if_missing(
        "import_queue/README.md",
        """
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
        """
    )

    # --- .gitkeep in key leaf dirs to keep them in git when empty ---
    gitkeep_dirs = [
        "data/locations",
        "data/npcs",
        "data/factions",
        "data/stories",
        "data/sessions",
        "data/items",
        "site/pages/locations",
        "site/pages/npcs",
        "site/pages/factions",
        "site/pages/stories",
        "site/pages/sessions",
        "ai/configs",
        "ai/prompts",
        "ai/work_queue",
        "ai/output",
        "ai/logs",
        "import_queue/npcs",
        "import_queue/npcs/valaria_eldenhold",
        "import_queue/npcs/mireholm",
        "import_queue/npcs/sylvara",
        "import_queue/locations",
        "import_queue/stories",
        "import_queue/sessions",
    ]

    for d in gitkeep_dirs:
        keep = root / d / ".gitkeep"
        if not keep.exists():
            keep.write_text("", encoding="utf-8")

    print(f"Initialized/verified SunspireOnlinePublic structure at: {root}")


if __name__ == "__main__":
    main()
