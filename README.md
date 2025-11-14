````markdown
# Sunspire Online – Public World Repository

This repository contains the **player-facing** world data and site structure for the **Sunspire** campaign.

It is designed as the public mirror of the private Sunspire workspace, which lives separately on the DM’s machine. This repo holds only material that is safe for players and the public to see.

---

## Repository Structure

```text
/data
  locations/   # JSON for cities, regions, locations (public-safe view)
  npcs/        # Public-facing NPC profiles
  factions/    # Public factions and organizations
  stories/     # Player-visible stories, vignettes, and lore
  sessions/    # Session summaries and timelines (spoiler-safe)
  items/       # Public artifacts, items, and curios

/site
  assets/      # Images, icons, and other static assets
  pages/       # Markdown/HTML/JS for the public-facing site

/docs
  roadmap/     # Project roadmaps and step-by-step build guides

/ai
  configs/     # AI configuration files (models, modes, routing)
  prompts/     # Prompt templates and formats for AI-assisted tools
````

At this stage, many folders may be empty or partially filled. The structure is intentionally in place **before** data is populated.

---

## Data Flow Overview

The world data in `/data` is intended to be:

1. Authored and organized in the DM’s private workspace (e.g. Notion, local files).
2. Exported and transformed into canonical JSON (private + public variants).
3. Filtered so that only **public-safe** records are copied into this repo.
4. Used by the site and AI tools to power:

   * Interactive maps
   * NPC / faction / location reference
   * Session summaries and story recaps

Private-only notes, red-text truths, and future plot hooks are **never** stored in this repository.

---

## Public vs Private

This repo is:

* **Public-facing**
* Safe for players to browse
* Safe to integrate into websites, tools, and viewers

The DM’s private environment (which contains:

* Full notes
* Spoilers
* Hidden factions
* Raw Notion exports
* Internal tools & experiments

…lives in a separate, non-public location and is **not** part of this repository.

---

## Roadmap & Documentation

The full project roadmap and step-by-step build plan are in:

* `docs/roadmap/0_Roadmap_Sunspire_Pipeline.md`
* `docs/roadmap/Step01_Repo_and_Structure.md`
* `docs/roadmap/Sunspire_Roadmap.md`
* `docs/roadmap/CHATGPT_Sunspire_Online_Roadmap.md`

These documents describe:

* How the repo is structured
* How data moves from private tools into this public mirror
* How AI and site components are expected to interact with the data

---

## Status

This repository is currently in the **initial structure** phase:

* Folder layout is established.
* Roadmap files are in place.
* Data folders are ready to receive curated JSON from the private toolchain.

As the campaign and tools evolve, this repo will be updated with new public-safe data, pages, and AI configurations.

````
