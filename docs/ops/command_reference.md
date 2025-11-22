# Sunspire Online – Command & Script Reference

This document tracks the recurring commands used to move data from the private Sunspire workspace (`D:\Tracy`) into the public repository (`D:\SunspireOnlinePublic`), and to maintain the repo.

It is **not** for lore – it is purely operational.

---

## Related Docs

- `docs/data_model.md` – JSON schemas for locations, NPCs, factions, stories, etc.
- `docs/file_index.md` – High-level file map for the public repo.
- `docs/world_hierarchy.md` – Canonical world → nation → city → site structure and IDs.

---

## 1. Notion → JSON Conversion (Private Side)

Run from: `D:\Tracy`  
Core utilities live in: `D:\Tracy\tools\utilities\`

### 1.1 Convert Notion CSV exports to JSON preview

```powershell
cd D:\Tracy

$in  = "D:\Tracy\docs\Notion Extract\Sunspire\Sunspire\Technical stuff\Archives"
$out = "D:\Tracy\data\notion_json_preview"

python tools\utilities\convert_notion_exports.py --input "$in" --out "$out"
````

**Typical outputs (examples):**

* `D:\Tracy\data\notion_json_preview\sessions_public.json`
* `D:\Tracy\data\notion_json_preview\factions_public.json`
* `D:\Tracy\data\notion_json_preview\factions_dm_only.json`
* `D:\Tracy\data\notion_json_preview\regions_public.json`
* `D:\Tracy\data\notion_json_preview\npcs_public.json`

---

## 2. Factions – Public vs DM-only

The converter creates:

* `factions_full.json` – all factions
* `factions_public.json` – **player-safe** factions
* `factions_dm_only.json` – DM-only factions (tagged as such in Notion)

**Rule:**
Only `factions_public.json` is ever copied into the public repo.

---

## 3. Copy Clean JSON into the Public Repo

All of this happens from `D:\Tracy`, copying into `D:\SunspireOnlinePublic`.

### 3.1 Valeris factions (example)

```powershell
# From: private preview
$src = "D:\Tracy\data\notion_json_preview\factions_public.json"

# To: public repo
$dst = "D:\SunspireOnlinePublic\data\factions\valeris_factions.json"

Copy-Item $src $dst -Force
```

### 3.2 Main campaign sessions (example)

```powershell
$src = "D:\Tracy\data\notion_json_preview\sessions_public.json"
$dst = "D:\SunspireOnlinePublic\data\sessions\main_campaign_sessions.json"

Copy-Item $src $dst -Force
```

**Pattern for other categories:**

```powershell
Copy-Item "D:\Tracy\data\notion_json_preview\<thing>_public.json" `
          "D:\SunspireOnlinePublic\data\<category>\<meaningful_name>.json" -Force
```

After adding any new file, update `docs/file_index.md`.

---

### 3.3 Split regions into per-nation location files

Script (runs in `D:\Tracy`):

* Path: `tools\utilities\split_regions_by_nation.py`
* Source: `D:\Tracy\data\notion_json_preview\regions_public.json`
* Output: short-name per-nation files in the public repo:

  * `D:\SunspireOnlinePublic\data\locations\valeria_locations.json`
  * `D:\SunspireOnlinePublic\data\locations\mireholm_locations.json`
  * `D:\SunspireOnlinePublic\data\locations\sylvara_locations.json`
  * …and other nation files

```powershell
cd D:\Tracy
python tools\utilities\split_regions_by_nation.py
```

Notes:

* Valeria bucket matches keywords: `valeria`, `valerian`, `valeris` (legacy), `eldenhold`.
* Mireholm / Sylvara buckets match `mireholm`, `sylvara` in name/association/tags/category.
* After running, commit the updated JSONs from `D:\SunspireOnlinePublic\data\locations\`.

---

### 3.4 Extract world nations

Script:

* Path: `D:\Tracy\tools\utilities\extract_world_nations.py`
* Source: `D:\Tracy\data\notion_json_preview\regions_public.json`
* Output: `D:\SunspireOnlinePublic\data\locations\world_nations.json`

```powershell
cd D:\Tracy
python tools\utilities\extract_world_nations.py
```

This produces a single record per nation (Category includes “Nation”), even if that nation does not yet have its own `*_locations.json` file.

---

### 3.5 Prepare per-nation location files

Script:

* Path: `D:\Tracy\tools\utilities\prepare_nation_location_files.py`
* Sources:

  * `D:\Tracy\data\notion_json_preview\regions_public.json`
  * `D:\SunspireOnlinePublic\data\locations\world_nations.json`
* Output:

  * `D:\SunspireOnlinePublic\data\locations/<slug>_locations.json` for each nation
  * `D:\SunspireOnlinePublic\data\locations\big_titty_demon_island.json`

```powershell
cd D:\Tracy
python tools\utilities\prepare_nation_location_files.py
```

---

## 4. Location Schema Maintenance

The public location JSONs under `data/locations/` are kept in sync with the canonical schema and world hierarchy using:

* `docs/data_model.md` – Location schema (fields, types, links)
* `docs/world_hierarchy.md` – Canonical world → nation → city → site IDs and names
* `tools/update_locations_schema.py` – Batch normalizer for location files

To re-normalize locations after adding or renaming things:

```powershell
cd D:\SunspireOnlinePublic
python tools\update_locations_schema.py
```

This script:

* Applies canonical IDs, categories, regions, parent IDs, `map_id`, and `tags`
* Merges aliases (including misspellings and long-form titles)
* Preserves original fields like `NameEntity_Name`, `Bounds`, and `Map`

After running:

```powershell
git status
git diff
```

Review changes and commit when satisfied.

#### Promote city sites (Eldenhold, Gravenhollow)

All building-level locations in:

- `data/locations/valeria_locations.json` → belong to Eldenhold  
- `data/locations/mireholm_locations.json` → belong to Gravenhollow  

To convert these "raw" building entries into proper `site` locations under their cities:

```powershell
cd D:\SunspireOnlinePublic
python tools\promote_city_sites.py
```

This script:

- Assigns IDs like `loc_eldenhold_<slug>_site` or `loc_gravenhollow_<slug>_site`
- Sets `category = "site"` and `type = "location"`
- Sets `parent_location_id` appropriately (`loc_eldenhold_city` / `loc_gravenhollow_city`)
- Preserves legacy fields such as `NameEntity_Name`, `Bounds`, and `Map`

---

#### Validate all locations

To check for structural issues (missing IDs, bad parents, invalid categories):

```powershell
cd D:\SunspireOnlinePublic
python tools\validate_locations.py
```

The script reports:

- **[FATAL]** – invalid JSON or unreadable files  
- **[ERROR]** – missing IDs, invalid categories, bad parent IDs, etc.  
- **[WARN]** – softer issues (missing map_id, missing region, etc.)  

Run this after any large change to `data/locations/` to confirm consistency.


---

## 5. Git – Basic Workflow for This Repo

Run from: `D:\SunspireOnlinePublic`

### 5.1 Check status

```powershell
git status
```

### 5.2 Stage changes

Stage everything:

```powershell
git add -A
```

or specific files:

```powershell
git add data\locations\valeria_locations.json
```

### 5.3 Commit with a message

```powershell
git commit -m "Describe what changed here"
```

### 5.4 Push to GitHub

```powershell
git push
```

### 5.5 Pull updates (if something changed on GitHub)

```powershell
git pull --rebase
```

---

## 6. Directory Overview (Operational)

* **Private workspace (DM-only)** – `D:\Tracy`

  * Raw Notion exports
  * Full JSON (including DM-only content)
  * Conversion / split scripts
  * DM notes, spoilers, internal tools

* **Public repo clone (player-safe)** – `D:\SunspireOnlinePublic`

  * `/data/` – only public-facing JSON
  * `/docs/` – roadmap, file index, command reference, world hierarchy
  * `/site/` – public web content (future)
  * `/tools/` – public-side maintenance scripts (e.g. `update_locations_schema.py`)
