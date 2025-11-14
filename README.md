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
