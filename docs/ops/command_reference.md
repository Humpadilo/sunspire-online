## Step 1: Make the folder & file

## Related Docs

- `docs/data_model.md` – JSON schemas for locations, NPCs, factions, stories, etc.
- `docs/file_index.md` – High-level file map for the public repo.

### Location Reference
- `docs/world_hierarchy.md` – Canonical world → nation → city → site structure. Use these names and IDs when creating or updating location JSON.

In PowerShell:

```powershell
cd D:\SunspireOnlinePublic

mkdir docs\ops -Force

' ' | Set-Content docs\ops\.gitkeep
```

Then create:

```text
D:\SunspireOnlinePublic\docs\ops\command_reference.md
```

Paste this into it:

````markdown
# Sunspire Online – Command & Script Reference

This document tracks the recurring commands used to move data from the private Sunspire workspace (`D:\Tracy`) into the public repository (`D:\SunspireOnlinePublic`), and to maintain the repo.

It is **not** for lore – it is purely operational.

---

## 1. Notion → JSON Conversion (Private Side)

Run from: `D:\Tracy`  
Scripts live in: `D:\Tracy\tools\utilities\`

### 1.1 Convert Notion CSV exports to JSON

```powershell
cd D:\Tracy

$in  = "D:\Tracy\docs\Notion Extract\Sunspire\Sunspire\Technical stuff\Archives"
$out = "D:\Tracy\data\notion_json_preview"

python tools\utilities\convert_notion_exports.py --input "$in" --out "$out"
````

**Output (example):**

* `D:\Tracy\data\notion_json_preview\sessions_public.json`
* `D:\Tracy\data\notion_json_preview\factions_public.json`
* `D:\Tracy\data\notion_json_preview\factions_dm_only.json`
* `D:\Tracy\data\notion_json_preview\regions_public.json`
* `D:\Tracy\data\notion_json_preview\npcs_public.json`
* plus matching `*_full.json` and `*_dm_only.json` where applicable.

---

## 2. Factions – Public vs DM-only

The converter creates:

* `factions_full.json` – all factions
* `factions_public.json` – public-only factions
* `factions_dm_only.json` – DM-only factions (tagged `DM`)

**Rule:**
Only `factions_public.json` is ever copied into the **public repo**.

---

## 3. Copy Clean JSON into the Public Repo

### 3.1 Valeris Factions

```powershell
# From: private data preview
$src = "D:\Tracy\data\notion_json_preview\factions_public.json"

# To: public repo
$dst = "D:\SunspireOnlinePublic\data\factions\valeris_factions.json"

Copy-Item $src $dst -Force
```

### 3.2 Main Campaign Sessions

```powershell
$src = "D:\Tracy\data\notion_json_preview\sessions_public.json"
$dst = "D:\SunspireOnlinePublic\data\sessions\main_campaign_sessions.json"

Copy-Item $src $dst -Force
```

As new regions, NPCs, stories, or items are added, follow the same pattern:

```powershell
Copy-Item "D:\Tracy\data\notion_json_preview\<something>_public.json" `
          "D:\SunspireOnlinePublic\data\<category>\<meaningful_name>.json" -Force
```

Update `docs/file_index.md` when new files are added.

---

### 3.3 Split regions into per-nation location files

Script (private side):

- Path: `D:\Tracy\tools\utilities\split_regions_by_nation.py`
- Source: `D:\Tracy\data\notion_json_preview\regions_public.json`
- Output (public repo):

  - `D:\SunspireOnlinePublic\data\locations\valeria_locations.json`
  - `D:\SunspireOnlinePublic\data\locations\mireholm_locations.json`
  - `D:\SunspireOnlinePublic\data\locations\sylvara_locations.json`

Run:

```powershell
cd D:\Tracy
python tools\utilities\split_regions_by_nation.py

Notes:

* Valeria bucket matches keywords: valeria, valerian, valeris (legacy), and eldenhold.
* Mireholm and Sylvara buckets match mireholm and sylvara in name/association/tags/category.
* After running this, commit the updated JSONs from D:\SunspireOnlinePublic\data\locations\.


That locks in:

- The script name  
- Where it reads from  
- What files it writes  
- The fact that Eldenhold is folded into Valeria on purpose

---

## 3️⃣ Git these doc edits

From `D:\SunspireOnlinePublic`:

```powershell
git add docs\file_index.md docs\ops\command_reference.md
git commit -m "Update docs for Valeria naming and location split behavior"
git push


### 3.4 Extract list of all nations

Script:

- Path: `D:\Tracy\tools\utilities\extract_world_nations.py`
- Source: `D:\Tracy\data\notion_json_preview\regions_public.json`
- Output: `D:\SunspireOnlinePublic\data\locations\world_nations.json`

Run:

```powershell
cd D:\Tracy
python tools\utilities\extract_world_nations.py

This file contains one record per nation (Category includes "Nation"), including Valeria, Mireholm, Sylvara, Greenhollow, Deadlands, etc., even if they do not yet have separate location files.

Then commit docs:

```powershell
cd D:\SunspireOnlinePublic
git add docs\file_index.md docs\ops\command_reference.md
git commit -m "Document world_nations.json and nation extraction script"
git push

### 3.5 Prepare per-nation location files

Script:

- Path: `D:\Tracy\tools\utilities\prepare_nation_location_files.py`
- Sources:
  - `D:\Tracy\data\notion_json_preview\regions_public.json`
  - `D:\SunspireOnlinePublic\data\locations\world_nations.json`
- Output:
  - `D:\SunspireOnlinePublic\data\locations/<slug>_locations.json` for each nation
  - `D:\SunspireOnlinePublic\data\locations/big_titty_demon_island.json`

Run:

```powershell
cd D:\Tracy
python tools\utilities\prepare_nation_location_files.py


## 4. Git – Basic Workflow for This Repo

Run from: `D:\SunspireOnlinePublic`

### 4.1 Check status

```powershell
git status
```

### 4.2 Stage changes

```powershell
git add .
```

or specific files:

```powershell
git add data\factions\valeris_factions.json
```

### 4.3 Commit with a message

```powershell
git commit -m "Add public Valeris faction data"
```

### 4.4 Push to GitHub

```powershell
git push
```

### 4.5 Pull changes from GitHub (if you edited there)

```powershell
git pull --rebase
```

---

## 5. Directory Overview (Operational)

* **Private workspace (DM-only):**
  `D:\Tracy`

  * Raw Notion exports
  * Full JSON (including DM-only)
  * Conversion scripts
  * DM notes, spoilers, internal tools

* **Public repo clone (player-safe):**
  `D:\SunspireOnlinePublic`

  * `/data/` – only `*_public`-derived JSON
  * `/docs/` – roadmap + this command reference + file index
  * `/site/` – public web content
  * `/ai/` – public-facing AI configs & prompts

````

---

## Step 2: Commit & push this

```powershell
cd D:\SunspireOnlinePublic

git add docs\ops\command_reference.md docs\ops\.gitkeep
git commit -m "Add operational command reference doc"
git push
````