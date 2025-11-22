# Sunspire Online – Data Model

This document defines the **public-facing JSON model** for Sunspire Online.

Root: `D:\SunspireOnlinePublic`

Public content lives in:

- `/data` – structured JSON
- `/site/pages` – Markdown lore
- `/docs` – project docs (like this one)

The private DM vault (`D:\Tracy`) is **not** covered here.

---

## 1. Core Principles

1. **JSON-first structure**

   Every lore object (location, NPC, faction, story, session, item) is a JSON object in `/data/**`.

2. **One object per entity**

   Default rule: one JSON object = one entity.

   - **Exception:** Existing *location bundles*:
     - `data/locations/world_nations.json`
     - `data/locations/<region>_locations.json`
     
     These may contain **arrays** of location objects. That’s allowed as long as each object still has a proper `id`.

3. **Stable IDs**

   - IDs never change, even if the `name` changes.
   - Always lowercase snake-like strings with type prefix:

     - `loc_valeria_nation`, `loc_eldenhold_city`
     - `npc_dark_bronson`
     - `faction_valeris_trade_bloc`
     - `story_battle_of_the_bards`
     - `session_S05`
     - `item_sunspire_relic_heartstone`

4. **Explicit links**

   No guessing from strings. Use IDs:

   - `home_location_id`
   - `primary_location_id`
   - `base_location_ids`
   - `faction_ids`
   - `related_npc_ids`
   - `story_ids`, `session_ids`, etc.

5. **JSON vs Markdown**

   - JSON = short, structured, machine-friendly.
   - Markdown = longform lore.
   - JSON points to Markdown via paths relative to repo root.

6. **Tags**

   - `tags` is always an array of short, lowercase strings.
   - Use tags for themes, tone, narrative role, and classification (`capital_city`, `cosmic_horror`, `political_intrigue`, etc.).

---

## 2. Folder Layout (Public Repo)

```text
/ai/
  prompts/
  work_queue/
  output/
  logs/

/data/
  locations/
  npcs/
  pcs/
  factions/
  stories/
  sessions/
  items/

/import_queue/
  locations/
  npcs/
    valeria_eldenhold/
    mireholm/
    sylvara/
  sessions/
  stories/

/site/
  assets/
  pages/
    locations/
    npcs/
    factions/
    stories/
    sessions/
    items/

/docs/
  README.md
  data_model.md
  file_index.md
  world_hierarchy.md
  ops/
    command_reference.md
  roadmap/
    README.md
    Sunspire_Online_Roadmap.md
    CHATGPT_Sunspire_Online_Roadmap.md
    Step01_Repo_and_Structure.md
    0_Roadmap_Sunspire_Pipeline.md
