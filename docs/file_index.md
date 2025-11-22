# Sunspire Online – File Index

This document tracks **important Python and JSON files** in the public repo.
Use it to remember what exists, where it lives, and what it does.

For schemas and canonical IDs, also see:

* `docs/data_model.md`
* `docs/world_hierarchy.md` 

---

## Tools (Python)

All public-side maintenance scripts live under `tools/`. 

| File                               | Purpose                                                                                           | Notes                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| `tools/init_sunspire_public.py`    | Scaffolds the public repo structure (folders, readmes, gitkeeps).                                 | Run after a fresh clone or when structure drifts.          |
| `tools/dump_repo_tree.py`          | Dumps a filtered repo tree + flat file list into `docs/file_inventory/`.                          | Used to rebuild this index without eyeballing everything.  |
| `tools/update_locations_schema.py` | Normalizes all location JSONs to match canonical schema + hierarchy.                              | Fixes IDs, parents, tags, categories in bulk.              |
| `tools/promote_city_sites.py`      | Promotes building/site entries inside nation files into proper `site` locations with parents/IDs. | Mostly for Eldenhold/Gravenhollow-style city submaps.      |
| `tools/validate_locations.py`      | Validates `data/locations/*.json` for structural errors.                                          | Run after big edits to catch duplicates/bad parents.       |

---

## Locations

All public location JSON files live under `data/locations/`. 
Each file contains one or more `location` objects.

| File                                         | Scope                | Notes                                                                           |
| -------------------------------------------- | -------------------- | ------------------------------------------------------------------------------- |
| `data/locations/world_locations.json`        | World                | Top-level Sunspire world record (`loc_sunspire_world`), parent for everything.  |
| `data/locations/world_nations.json`          | World                | High-level list of nations / major regions.                                     |
| `data/locations/valeria_locations.json`      | Valeria (nation)     | Valeria plus cities/sites/POIs (Eldenhold lives here right now).                |
| `data/locations/mireholm_locations.json`     | Mireholm (nation)    | Mireholm plus related locations (Gravenhollow etc.).                            |
| `data/locations/sylvara_locations.json`      | Sylvara (nation)     | Nation record only so far.                                                      |
| `data/locations/deadlands_locations.json`    | Deadlands (nation)   | Nation record (future expansion).                                               |
| `data/locations/greenhollow_locations.json`  | Greenhollow (nation) | Nation record (future expansion).                                               |
| `data/locations/karak_thul_locations.json`   | Karak Thul (nation)  | Nation record (future expansion).                                               |
| `data/locations/skraggmar_locations.json`    | Skraggmar (nation)   | Nation record (future expansion).                                               |
| `data/locations/thra_zul_locations.json`     | Thra’Zul (nation)    | Nation record (future expansion).                                               |
| `data/locations/xorath_kul_locations.json`   | Xorath Kul (nation)  | Nation record (future expansion).                                               |
| `data/locations/big_titty_demon_island.json` | BTDI (region)        | Special region file containing region + child region + site.                    |

> Rule: Nation/region files follow `data/locations/<slug>_locations.json`.
> BTDI is a special case because it’s a standalone region package.

---

## Factions

Public faction JSON lives under `data/factions/`. 

| File                                  | Region/Nation | Notes                                              |
| ------------------------------------- | ------------- | -------------------------------------------------- |
| `data/factions/valeris_factions.json` | Valeria       | Public-safe faction set. Naming kept in-universe.  |

---

## Sessions

Session summaries live under `data/sessions/`. 

| File                                        | Scope         | Notes                                                          |
| ------------------------------------------- | ------------- | -------------------------------------------------------------- |
| `data/sessions/main_campaign_sessions.json` | Main campaign | Public-safe list and summaries of the main Sunspire sessions.  |

---

## NPCs

Canonical NPC JSON will live under `data/npcs/`. Folder exists but not populated yet. 

| File         | Scope | Notes                                                  |
| ------------ | ----- | ------------------------------------------------------ |
| *(none yet)* | —     | NPCs are currently staged in import queue (see below). |

---

## Stories / Vignettes

Canonical story JSON will live under `data/stories/`. Folder exists but empty. 

| File         | Scope | Notes                                            |
| ------------ | ----- | ------------------------------------------------ |
| *(none yet)* | —     | Story generation pipeline comes later (AI step). |

---

## Items / Artifacts

Canonical item JSON will live under `data/items/`. Folder exists but empty. 

| File         | Scope | Notes                                                |
| ------------ | ----- | ---------------------------------------------------- |
| *(none yet)* | —     | Items/artifacts will be migrated after NPC baseline. |

---

## Import Queue (Staging)

Anything in `import_queue/` is **raw input waiting to be converted into canonical JSON**. 

| File                                                    | Type                | Intended Destination | Notes                                                              |
| ------------------------------------------------------- | ------------------- | -------------------- | ------------------------------------------------------------------ |
| `import_queue/npcs/valeria_eldenhold/Eldenhold_NPC.csv` | Notion export (CSV) | `data/npcs/*.json`   | Valeria/Eldenhold NPCs + Champions mixed in. Needs split/convert.  |
| `import_queue/locations/`                               | folder              | `data/locations/`    | Placeholder for future CSV/JSON drops.                             |
| `import_queue/sessions/`                                | folder              | `data/sessions/`     | WhisperX merged outputs land here before promotion.                |
| `import_queue/stories/`                                 | folder              | `data/stories/`      | Placeholder for AI story drafts before promotion.                  |

---

## Notes

* **DM-only** files live in private (`D:\Tracy`) and never go public.
* When adding a new important JSON or tool, update this index with:

  * filename/path
  * scope
  * short description
* Keep filenames consistent with `docs/world_hierarchy.md` and `docs/data_model.md`.

---