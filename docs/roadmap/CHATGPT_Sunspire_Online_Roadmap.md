# Sunspire Online – AI Pipeline Readme

This document explains **how the AI side of Sunspire Online works**, how everything plugs together, and how future you (or future AIs) should interact with the system.

This is the companion to the main Sunspire_Roadmap. That one tells *you* what to do. This one tells the **AI workers**, coders, and supporting scripts what rules they must follow.

---

# 1. Purpose of the AI System

The AI is not the DM. It is the world’s **scribe, bureaucrat, gossip merchant, and creative intern**. Its primary jobs:

* Generate structured lore (NPCs, factions, events, vignettes)
* Maintain consistency with the JSON data model
* Use tagging, linking, and world-state data
* Avoid contradictions with canon
* Produce content that can be reviewed before publication
* Help automate world updates and story expansions

The AI worker(s) will read from the public GitHub repository, write draft content locally, and only promote approved results.

---

# 2. AI Responsibilities

## 2.1 Structured Lore Generation

The AI produces:

* NPC vignettes
* Backstories
* Relationship maps
* Location flavor text
* Plot hooks
* Rumor-board entries
* Session-based world updates

Everything generated must:

* Follow the JSON specs in `docs/data_model.md`
* Use Markdown for long-form text
* Match IDs, links, and file paths in the repo

## 2.2 World-State Awareness

AI must:

* Read all relevant `/data/**` JSON files
* Read referenced Markdown when needed
* Use tags from `data/tags.json`
* Respect timeline (sessions, pre/post events)

## 2.3 Draft-Only Output

Generated content goes to:

```
/ai/output/<task_id>/
```

Until human review. Approved files get promoted to:

```
/data/<type>/
/site/pages/<type>/
```

Nothing overwrites canon without approval.

---

# 3. AI Folder Structure

```
/ai/
  configs/        # Task definitions
  prompts/        # Prompt templates
  work_queue/     # Pending tasks
  output/         # Draft results
  logs/           # Optional: run history
```

### configs/

Defines each task type, including:

* required inputs
* output format
* allowed fields
* safety constraints

### prompts/

Text templates the AI fills in using structured context.

### work_queue/

Each file describes a single task:

```json
{
  "task_type": "generate_npc_vignette",
  "npc_id": "npc_elyssa_dorne",
  "location_id": "loc_valeria_city",
  "tone": "political_intrigue"}
```

### output/

Draft JSON + Markdown produced by the AI.

---

# 4. Task Types

## 4.1 NPC Vignette Generation

Input:

* NPC JSON
* Location JSON
* Related factions
* Previous stories

Output:

* Story JSON
* Markdown text
* Updated NPC hooks

## 4.2 Location Flavor Expansion

AI adds/update:

* rich textual detail
* cultural notes
* local rumors
* sensory imagery

## 4.3 NPC Relationship Mapping

Given several NPCs in a location, AI produces:

* relationships
* alliances
* conflicts
* plot hooks connecting them

## 4.4 Session-Based World Reactions

AI updates:

* rumors
* world events
* consequences

This lets the world evolve automatically.

---

# 5. Canon Rules

The AI must obey:

1. **Do not contradict existing JSON.**
2. **Do not rename IDs.**
3. **Do not invent major events** unless the task config explicitly allows it.
4. **Always use tags from the registry** when available.
5. **Only propose new tags** through:

```
/ai/output/proposed_tags.json
```

6. **Never overwrite human-written Markdown** unless instructed.
7. **Never delete files.**

---

# 6. Tag Registry Rules

AI must load:

```
/data/tags.json
```

When generating content:

* Prefer existing tags
* Suggest new tags only when necessary
* Place suggestions in proposed list

---

# 7. Input Requirements

AI scripts must gather:

* NPC JSON + linked locations
* All related stories
* Relevant session summaries
* Related factions
* Tag registry

If something is missing, log it and abort the task gracefully.

---

# 8. Output Requirements

AI output must include:

* Valid JSON matching schema
* Markdown files for long content
* No broken links
* No placeholder text

If the AI is unsure, it must:

* leave a `"confidence": <0–1>` field
* never guess canon

---

# 9. Pipeline Lifecycle

## 9.1 Task Added

Human or helper script creates a file in `/ai/work_queue`.

## 9.2 AI Worker Runs

* Loads config
* Loads prompt template
* Builds context bundle
* Generates output
* Writes to `/ai/output/<task_id>`

## 9.3 Human Review

Human approves or rejects.

## 9.4 Promotion

Approved content is moved into canonical folders.

---

# 10. How Other AIs Should Behave

This doc tells all AIs working inside this project:

* What files mean
* What constraints must be followed
* What structured formats exist
* How not to break the world

Any new AI assistant should be told:

> "Read `Sunspire_AI_Readme` and follow its rules when generating, modifying, or interpreting Sunspire data."

---

# 11. Future Extensions (Optional)

* Live session listener feeding scene/state updates
* AI-managed tavern/rumor engine
* AI-run downtime scenes
* Real-time NPC chatter
* Dynamic world events
* Enemy-AI combat controller

These belong in extended configs under `/ai/configs/next/` when implemented.

---

# 12. Summary

This Readme defines:

* AI responsibilities
* Folder structure
* Task rules
* Output formats
* Canon constraints

Follow it and the Sunspire world stays consistent, evolving, and organized.
