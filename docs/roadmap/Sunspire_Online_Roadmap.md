## Sunspire Online

Step- 0 Roadmap
Step- 1 Repository & Structure
Step- 2 Data Model
Step- 3 Migration
Step- 4 Public Site
Step- 5 AI Pipeline
Step- 6 Ongoing Workflow

----------------------------
----------------------------

# 0.1 — Purpose of This Pipeline
Your endgame is to build a fully automated knowledge ecosystem powering:
⦁	  Public wiki
⦁	  Public interactive map
⦁	  JSON + Markdown backbone
⦁	  Private→public migration system
⦁	  Local AI worker that generates stories

# 0.2 — The Six Major Steps
1.	Repo & structure
2.	Data model
3.	Lore migration
4.	Public site
5.	AI pipeline Workflow

# 0.3 — Why This Order Works
You build the home → define the language → move your stuff → decorate → hire AI → write maintenance manual.

# 0.4 — Project Scope Overview
Public repo: JSON/MD, site, map, docs.
Private repo: DM notes, raw exports, spoilers, TracyDND.

# 0.5 — What Success Looks Like
Live site, stable JSON model, migration working, map connected, AI generating, workflow established.


# 0.6 — Future Expansions
Map hierarchy, scene engine, timeline mode, galleries, quest boards, AI memory integration.

# 0.7 — Checklist
⦁	Understand pipeline
⦁	Know order
⦁	Know public vs private
Ready for Step 1

----------------------------
----------------------------

# Step 1 – Create the Public GitHub Repo & Structure

**Goal:**  
Create a clean, public GitHub repository that will hold all *player-safe* Sunspire content: JSON data, Markdown lore, the public site, and roadmap docs.

This is the “public bookshelf” for Sunspire. Your private `D:\Tracy` setup stays as the DM vault.

When Step 1 is done, you will have:
* A public GitHub repo (e.g., `sunspire-online-public`)
* A cloned local folder (e.g., `D:\SunspireOnlinePublic`)
* A basic, intentional folder layout: `/data`, `/site`, `/docs`, `/ai`
* The roadmap + Step files checked into `/docs/roadmap`


# 1.2 – Decide What Is Public vs Private--- Complete

Before you even open GitHub, decide what *belongs* in the public repo.

**Public repo should contain:**
* Player-safe lore and world info:
  * Regions, nations, cities, locations
  * High-level factions (no twist reveals)
  * Public-facing NPC detail (what players can know or infer)
* Long-form player-safe text:
  * Stories that have already “happened” in play
  * Background lore that doesn’t reveal future plot
* Public assets:
  * Safe versions of maps
  * Art you are okay sharing
* Structural files:
  * JSON data used by the public site and AI
  * Markdown pages for the site
  * Roadmap docs like this one
  * AI configuration and prompt templates (no secrets)

**Keep in `D:\Tracy` (private only):**
* Full DM notes
* Spoilers and twist plans
* Red-text “truths” and secret motivations
* Raw Notion exports and intermediate junk
* Internal Tracy/TracyDND tooling, logs, and experiments

**Rule of thumb:**  
If a player could stumble into it by clicking around the site and it would ruin a surprise, it lives in private, not in the public repo.

# 1.3 – Create the GitHub Repository- Complete

1. Log into your GitHub account.
2. Click **New repository**.
3. Use a name like:
   * `sunspire-online`
4. Set **Visibility** to `Public`.
5. Initialize with:
   * A `README.md` (yes)
   * You can skip `.gitignore` and License for now, or add them later.
6. Click **Create repository**.

After it’s created:
* Copy the **HTTPS clone URL**. You’ll use this in a minute from PowerShell.
  https://github.com/Humpadilo/sunspire-online.git

# 1.4 – Create Local Folder and Clone the Repo- Complete

Pick a clean local path for the public repo. Suggested:

* `D:\SunspireOnlinePublic`

**Steps:**

1. Create the folder if it doesn’t exist.
2. Open PowerShell and run:
   * `cd D:\SunspireOnlinePublic`
   * `git clone <your_repo_url> .`
     * Note the `.` at the end to clone into the current folder.

When this is done, `D:\SunspireOnlinePublic` is your local working copy of the **public** repo, which is separate from `D:\Tracy`.

You will treat:
* `D:\Tracy` as your *source of truth* and DM vault.
* `D:\SunspireOnlinePublic` as the public mirror that receives cleaned, player-safe exports.

# 1.5 – Establish the Initial Folder Structure- Complete

In `D:\SunspireOnlinePublic`, create a simple, intentional layout.

Recommended starting structure:

```text
/data/
  locations/
  npcs/
  factions/
  stories/
  sessions/
  items/

/site/
  assets/
  pages/

/docs/
  roadmap/

/ai/
  configs/
  prompts/

README.md
```

**Roles:**

* `/data`  
  Canonical JSON data for the **public** world. Every location, NPC, faction, story, and session will eventually live here.

* `/site`  
  Files for the public-facing website (HTML, Markdown, templates, CSS, JS).

* `/docs`  
  Human-readable documentation, including:
  * This pipeline roadmap
  * Detailed step files (Step 0–6)
  * Any future technical notes

* `/ai`  
  High-level AI pipeline configuration:
  * `configs/` – JSON configs describing task types and settings
  * `prompts/` – prompt templates for different generation tasks

Don’t worry about filling these folders yet. Step 1 is just about **creating** the structure so everything has a home.


# 1.6 – Add Roadmap & Step Files to `/docs/roadmap`- Complete

Inside your public repo:

* Create: `/docs/roadmap/`

Then place:
* `0_Roadmap_Sunspire_Pipeline.md`
* `Step01_Repo_and_Structure.md`
* (and later) `Step02_...`, `Step03_...`, etc.

These are for **you and future helpers**, not players.

**Why bother?**
* This turns the repo into a self-documenting project.
* Any future AI, collaborator, or confused future-you can open `/docs/roadmap` and instantly see how everything works and what each step is for.


# 1.7 – Update the Root README.md

The root `README.md` should briefly explain:

* What this repo is
* What lives where
* What is public vs private

Example outline:

```markdown
# Sunspire Online – Public Lore Repository

This repository contains the **player-facing** world data and website for the Sunspire campaign.

## Structure

- `/data` – JSON data for locations, NPCs, factions, stories, sessions, and items.
- `/site` – Public website files (pages, assets, layout).
- `/docs/roadmap` – Internal documentation for how this repo is organized and maintained.
- `/ai` – Configuration and prompt templates for AI-assisted story generation.

## Private vs Public

DM-only content, spoilers, raw notes, and internal tools live in a separate private environment and are **not** part of this repository.
```

Keep it short and clear. The detailed process lives in `/docs/roadmap`.


# 1.8 – First Commit & Push

Once:
* The folder structure exists
* The roadmap docs are added
* The root `README.md` is updated

Do your first commit.

In PowerShell (inside `D:\SunspireOnlinePublic`):

1. `git status` – sanity check what’s new.
2. `git add .`
3. `git commit -m "chore: initialize public repo structure"`
4. `git push`

After this:
* Your public GitHub repo now has:
  * Clean folders
  * A clear root README
  * Roadmap docs
* Anyone (including your future self and any AI) can open the repo and immediately understand its purpose.


# 1.9 – What to Ask the “Code AI” Chat For (Later)

Step 1 doesn’t need any heavy scripting, but you can make future life easier by asking another AI chat to:

1. **Generate a good `.gitignore`**  
   * For:
     * Node-based static site tooling (if you adopt one later)
     * Python utilities
     * OS junk (`Thumbs.db`, etc.)

2. **Create a “structure check” script**  
   * A small Python script that:
     * Verifies that `/data`, `/site`, `/docs/roadmap`, `/ai` exist
     * Optionally creates them if they are missing
   * Helps guard against accidental deletions or misconfigurations.

3. **Optional: Repo bootstrap script**  
   * A script you can run on a *new* machine that:
     * Clones the repo
     * Ensures folders exist
     * Prints a quick summary of what’s inside.

None of this is required to finish Step 1, but they are nice add-ons after the basic structure is in place.

---

**Step 1 is “done” when:**
* Public repo exists on GitHub.
* Local clone exists (e.g., `D:\SunspireOnlinePublic`).
* `/data`, `/site`, `/docs/roadmap`, `/ai` are in place.
* Roadmap + Step 1 docs are inside `/docs/roadmap`.
* Root `README.md` explains the structure clearly.

----------------------------
----------------------------

# Step 2 – Data Model & Tagging Overview

**Goal:**  
Define a clear, AI-friendly data model for all Sunspire lore using JSON as the backbone, with Markdown for longer prose.

This step answers:
* “What does a *location* look like in JSON?”
* “How do we represent an *NPC*, a *story*, a *faction*, a *session*?”
* “Where does long text live vs structured fields?”
* “How do we tag things so AI can find relevant pieces quickly?”

When Step 2 is done:
* You have a single, documented **data model** for all entities.
* You know which folders in `/data` hold which entity type.
* You know how JSON and Markdown connect.
* Future scripts and AI prompts can rely on this structure.


# 2.2 – Core Principles of the Data Model

The rules of the game:

1. **JSON-first structure**
   * Each lore object (location, NPC, faction, story, session, item) is represented as a JSON document under `/data/...`.

2. **One object per file**
   * One file = one entity.
   * Easier to track in Git, easier to load selectively with scripts, easier for AI to reason about.

3. **Stable IDs**
   * Every object has an `id` that never changes, even if its `name` changes.
   * IDs are lowercase, snake-like strings with type prefixes:
     * `loc_eldenhold_city`, `npc_elyssa_dorne`, `faction_valerian_crown`, `story_bards_battle`.

4. **Explicit links between entities**
   * No guessing by free text.
   * Use fields like `home_location_id`, `faction_ids`, `participants`, `primary_location_id`, `session_ids`, etc.
   * Values are arrays of IDs, not names, wherever possible.

5. **Separation of structure vs prose**
   * JSON = short, structured, machine-friendly.
   * Markdown = longform descriptions, backstories, scenes, vignettes.
   * JSON points to Markdown via relative paths.

6. **Tagging for AI and humans**
   * Use `tags` arrays to capture themes, tones, roles, and “buckets” of content.
   * Tags should be short, lowercase, and stable across entities.

Stick to these principles and your AI life will be much easier.


# 2.3 – Entity Types and Where They Live

At minimum, support these entity types:

* `location` – regions, cities, districts, neighborhoods, dungeons, buildings, special sites.
* `npc` – non-player characters.
* `pc` – player characters (optional in public repo).
* `faction` – groups, organizations, cults, guilds, etc.
* `story` – discrete scenes, vignettes, short stories, background pieces.
* `session` – actual-play session summaries / recaps.
* `item` – important artifacts, relics, named objects.

Recommended folder mapping under `/data`:

```text
/data/
  locations/
    loc_*.json
  npcs/
    npc_*.json
  factions/
    faction_*.json
  stories/
    story_*.json
  sessions/
    session_*.json
  items/
    item_*.json
```

This way, type is reinforced both by:
* `type` field in JSON  
* filename and folder location


# 2.4 – Example JSON: Location & NPC

These examples are templates. You or future scripts can tweak them, but they show the general idea.

## Example: Location JSON

```json
{
  "id": "loc_eldenhold_city",
  "type": "location",
  "name": "Eldenhold",
  "category": "city",
  "region": "Sunspire Heartlands",
  "map_id": "sunspire_world",
  "tags": ["capital_city", "trade_hub", "player_hub"],
  "summary": "The bustling capital of the Sunspire Heartlands.",
  "detail_markdown": "site/pages/locations/eldenhold.md",
  "faction_ids": ["faction_merchants_guild", "faction_city_guard"],
  "related_npc_ids": ["npc_elyssa_dorne", "npc_captain_rovek"],
  "first_mentioned_session": "S01",
  "source_refs": [
    {"kind": "notion", "ref": "Eldenhold City Notion Page"},
    {"kind": "session", "ref": "S01"}
  ]
}
```

Notes:
* `category` distinguishes cities vs regions vs dungeons.
* `map_id` will later help the map engine know which map this belongs to.
* `detail_markdown` points to where the full text lives.

## Example: NPC JSON

```json
{
  "id": "npc_elyssa_dorne",
  "type": "npc",
  "name": "Elyssa Dorne",
  "role": "noble schemer",
  "home_location_id": "loc_eldenhold_city",
  "faction_ids": ["faction_merchants_guild"],
  "tags": ["noble", "schemer", "politics"],
  "public_summary": "A sharp-tongued noble with unclear loyalties.",
  "backstory_markdown": "site/pages/npcs/elyssa_dorne.md",
  "story_hook_ids": ["story_eldenhold_court_intrigue"],
  "source_refs": [
    {"kind": "notion", "ref": "NPC: Elyssa Dorne"},
    {"kind": "session", "ref": "S05"}
  ]
}
```

Notes:
* `role` is a short “design intent” for the NPC.
* `home_location_id` ties them to one main place.
* `story_hook_ids` can point to stories where this NPC plays a role.


# 2.5 – Example JSON: Story & Session

## Example: Story / Vignette JSON

```json
{
  "id": "story_eldenhold_court_intrigue",
  "type": "story",
  "title": "Whispers in the Court of Eldenhold",
  "participants": ["npc_elyssa_dorne", "npc_captain_rovek"],
  "primary_location_id": "loc_eldenhold_city",
  "tags": ["political_intrigue", "pre_session", "noble_conflict"],
  "timeline_hint": {
    "relative_to_session": "S05",
    "when": "before"
  },
  "text_markdown": "site/pages/stories/eldenhold_court_intrigue.md",
  "generated": false,
  "source_refs": [
    {"kind": "dm_story", "ref": "Elyssa & Rovek Court Seeds"}
  ]
}
```

Notes:
* `participants` references NPC/PC IDs.
* `timeline_hint` gives AI and humans context on when this occurs relative to sessions.
* `generated` can mark whether this came from AI or from you.

## Example: Session JSON

```json
{
  "id": "session_S05",
  "type": "session",
  "session_number": 5,
  "title": "Battle of the Bards",
  "date": "2025-03-10",
  "summary_markdown": "site/pages/sessions/session_S05_summary.md",
  "full_log_markdown": null,
  "key_location_ids": ["loc_ashenvale_town", "loc_drunken_wyvern_tavern"],
  "key_npc_ids": ["npc_bronson_dark", "npc_mruno_bandmate"],
  "tags": ["music", "competition", "chaos"],
  "source_refs": [
    {"kind": "audio", "ref": "Session05 recording"},
    {"kind": "transcript", "ref": "Session05 transcript"}
  ]
}
```

Notes:
* `summary_markdown` is the player-facing recap.
* You can keep full transcripts in private repos and only link summaries publicly.


# 2.6 – Tagging Strategy & Taxonomy

Tags are for:
* Quick filtering
* Thematic search
* AI context selection
* Organizing large amounts of content

Good tags are:
* Short
* Lowercase
* Reused, not invented fresh every time

Suggested tag categories:

**By theme:**
* `political_intrigue`
* `cosmic_horror`
* `folk_horror`
* `heroic_fantasy`
* `tragedy`
* `comedy`

**By location / environment:**
* `capital_city`
* `border_town`
* `swamp`
* `underdark`
* `temple`
* `tavern`

**By narrative role:**
* `intro_hook`
* `downtime_scene`
* `flashback`
* `aftermath`
* `foreshadowing`

**By visibility (for private models):**
* `player_safe`
* `dm_only`
* `spoiler_heavy`

In the **public** repo, avoid `spoiler_heavy` content altogether.  
You can still tag things conceptually (`political_intrigue`, `court_drama`, etc.).


# 2.7 – JSON vs Markdown: Who Does What?

**JSON is the index card.**  
**Markdown is the full page.**

JSON should handle:
* IDs and types
* Names and short summaries
* Tags and relationships
* Paths to Markdown files
* Simple fields that help AI know “what this is”

Markdown should handle:
* Long descriptions of locations
* Full NPC backstories
* Story text for vignettes and scenes
* Session recaps / writeups

Example pairing:

* `/data/npcs/npc_elyssa_dorne.json`
* `/site/pages/npcs/elyssa_dorne.md`

In the JSON:

```json
{
  "id": "npc_elyssa_dorne",
  "type": "npc",
  "name": "Elyssa Dorne",
  "backstory_markdown": "site/pages/npcs/elyssa_dorne.md",
  "tags": ["noble", "schemer", "politics"]
}
```

In the Markdown file:

```markdown
# Elyssa Dorne

Public-facing text about Elyssa's background, mannerisms, and role in Eldenhold.
(No major future spoilers.)
```

This lets:
* AI read structured info quickly
* Humans read actual lore
* The site render both cleanly


# 2.8 – Minimum Required Fields per Type

These are the fields that should always exist.

## Location

* `id` – stable ID, e.g., `loc_eldenhold_city`
* `type` – `"location"`
* `name`
* `category` – e.g., `city`, `region`, `tavern`, `dungeon`
* `tags` – array of tag strings
* Optional but recommended:
  * `map_id`
  * `summary`
  * `detail_markdown`
  * `faction_ids`

## NPC

* `id`
* `type` – `"npc"`
* `name`
* `role` – short design intent
* `home_location_id`
* `tags`
* Optional:
  * `faction_ids`
  * `backstory_markdown`
  * `story_hook_ids`

## Faction

* `id`
* `type` – `"faction"`
* `name`
* `scope` – e.g., `city`, `region`, `empire`
* `tags`
* Optional:
  * `base_location_ids`
  * `leader_npc_ids`
  * `ideology`

## Story

* `id`
* `type` – `"story"`
* `title`
* `participants` – NPC/PC IDs
* `primary_location_id`
* `tags`
* `text_markdown`

## Session

* `id` – e.g., `session_S05`
* `type` – `"session"`
* `session_number`
* `title`
* `date`
* `summary_markdown`
* `tags`

You can expand these later, but defining minimums now means your scripts and AI can treat all entities consistently.


# 2.9 – Writing the Data Model Doc in the Repo

Once you’re happy with the patterns in this step, consolidate them into one master reference file inside the public repo, for example:

* `/docs/data_model.md`

That file should include:
* Overview of entity types
* Example JSON for each type
* Required fields tables
* Tagging guidelines
* JSON vs Markdown rules

This becomes the **contract**:
* Scripts must follow it.
* AI prompts should assume it.
* Future modifications should update it.

Treat `/docs/data_model.md` as canon. If something in practice drifts from it, either:
* Fix the data, or
* Update the doc and then fix the data.


# 2.10 – What to Ask the “Code AI” Chat For

Once this data model is agreed on, another chat can help you with tools to enforce and use it.

Ask for:

1. **JSON Schema or Pydantic models**
   * For each type (`location`, `npc`, `faction`, `story`, `session`, `item`).
   * These can validate data, and provide auto-complete in editors.

2. **A validator script**
   * Walks `/data/**`
   * Loads every JSON file
   * Confirms:
     * required fields exist
     * field types are correct
     * IDs follow naming conventions
   * Prints a report of problems (missing fields, bad links, etc.).

3. **Link checker**
   * Ensures:
     * `home_location_id` values point to real locations.
     * `faction_ids` refer to actual faction JSONs.
     * `participants` only reference existing NPC/PC IDs.

4. **Tag analyzer**
   * Lists all tags in use.
   * Highlights entities with no tags or weird one-off tags.

These tools will be crucial during Step 3 (migration) and Step 5 (AI pipeline).

---

**Step 2 is “done” when:**
* You have a written, stable data model (`/docs/data_model.md`).
* You know the required fields and example JSON for each entity type.
* You understand how tags and Markdown work with JSON.
* You’re ready to start mapping your existing lore into this schema in Step 3.

----------------------------
----------------------------

# Step 3 – Migrate Existing Lore into the Public Repo

**Goal:**  
Take all the Sunspire world info scattered across Notion exports, TracyDND, session logs, and old files and move **player-safe** parts into the new `/data` + `/site/pages` structure in your public repo.

This is the “cleaning & shelving” phase:
* You are not rewriting the world.
* You are **mapping** it into the new data model from Step 2.
* You are splitting “DM-only” and “player-safe” as you go.

When Step 3 is done (or at least “good enough to move on”):
* You have real JSON files in `/data/locations`, `/data/npcs`, etc.
* You have Markdown in `/site/pages/...` linked from those JSONs.
* At least a subset of locations, NPCs, stories, and sessions are migrated and valid.


# 3.2 – Identify Your Source Buckets

From your existing `D:\Tracy` world, you have several major sources of lore:

* **Notion exports**  
  Under something like:  
  `docs\Notion Extract\Sunspire\Sunspire\Technical stuff\...`
  * Locations
  * Factions
  * NPC notes
  * Stories / vignettes
  * Lore articles

* **Campaign sessions**  
  Under your session logs and transcripts:
  * DM summaries
  * Full transcripts
  * Audio recordings

* **TracyDND lexicon / indexes**  
  * Terms, concepts, name references, etc.

Step 3 is not about migrating **everything at once**.  
It’s about migrating in controlled phases, starting with a core slice.


3.3 – Phased Migration Strategy
Do not attempt to migrate the entire lore library in one go. That way lies madness.
Instead, work in phases:
Phase 1 – World Structure
⦁	Core regions / nations
⦁	Main cities
⦁	A few key special locations (major dungeons, temples, hubs)
Phase 2 – People
⦁	Core NPCs related to those locations
⦁	Optional: PCs if you want them on the public site
Phase 3 – Stories & Vignettes
⦁	A small set of stories that:
⦁	Don’t spoil future campaigns
⦁	Help define tone for the world
Phase 4 – Sessions
⦁	Session summaries (not full logs)
⦁	Enough to show history, but not every detail immediately
After these four phases, you’ll already have enough content to:
⦁	Power the site
⦁	Give the AI useful context
⦁	Iterate without drowning.


# 3.4 – Define Mapping Rules from Source → Data Model

Before you touch scripts, write down **how** each source type maps into your JSON/Markdown model.

Example decisions:

* Notion “Location” pages → `/data/locations/*.json` + `/site/pages/locations/*.md`
  * Notion Title → `name`
  * Notion Category → `category`
  * Notion Body → Markdown text
  * Any “tags” or “type” fields → `tags`

* NPC pages → `/data/npcs/*.json` + `/site/pages/npcs/*.md`
  * Title → `name`
  * Field like “Role/Job” → `role`
  * Location field → `home_location_id` (via mapping name→id)
  * Body text → `backstory_markdown`

* Factions → `/data/factions/*.json`
  * Title → `name`
  * Region/scope field → `scope`
  * Motto/ideology fields → `ideology`
  * HQ location → `base_location_ids`

* Stories → `/data/stories/*.json` + `/site/pages/stories/*.md`
  * Title → `title`
  * Involved characters → `participants`
  * Location → `primary_location_id`

* Session summaries → `/data/sessions/*.json` + `/site/pages/sessions/*.md`
  * Session number → `session_number`
  * Summary → `summary_markdown`
  * Date → `date`

Write these mapping rules into a doc in the public repo, e.g.:

* `/docs/migration_mapping.md`

This becomes the contract for your conversion scripts.


# 3.5 – Separating Player-Safe from Spoilers

**Critical rule:**  
Do **not** blindly export all DM data into the public repo.

Strategies:

* Use your private environment (`D:\Tracy`, TracyDND, Notion) to:
  * Mark or tag pages as `player_safe` vs `dm_only`.
  * Or maintain two fields per object:
    * “Public summary” – safe
    * “DM notes” – private

* For each migrated entity:
  * Public JSON + Markdown contains **only** what you’re okay sharing.
  * DM truths stay in private storage.

* If in doubt:
  * Either **omit** it from public for now, or
  * Write a new redacted “public” version for the players.

Step 3 is an opportunity to **curate** as you migrate.


3.6 – Always Start with a Small Sample
For each source type, follow this pattern:
1.	Pick 3–5 examples:
⦁	Locations
⦁	NPCs
⦁	Stories
⦁	Sessions
2.	Manually or semi-manually convert them:
⦁	One example location JSON + Markdown
⦁	One NPC JSON + Markdown
⦁	One story JSON + Markdown
⦁	One session JSON + Markdown
3.	Adjust:
⦁	Tweak field names if they feel wrong.
⦁	Adjust where text should live (JSON vs Markdown).
⦁	Improve tags.
4.	Once the sample feels good and valid:
⦁	Then you ask another chat to help automate this mapping for the larger dataset.
This way you avoid:
⦁	Writing automation for a structure you later decide you don’t like.


# 3.7 – Using the “Code AI” to Build Conversion Scripts

Once you have:
* A clear data model (Step 2)
* Clear mapping rules (Step 3.4)
* A few good manual examples

Then ask the coding chat to:

> “Given this input format (CSV/Markdown from Notion) and this output JSON/Markdown structure, write a Python script that:
>  1. Reads an input file from `D:\Tracy`
>  2. Applies these mapping rules
>  3. Writes JSON into `/data/<type>/` in the public repo
>  4. Writes Markdown into `/site/pages/<type>/` and points to it from JSON.”

Do this **per type**, for example:
* One converter for locations.
* One for NPCs.
* One for stories.
* One for sessions.

You can later merge logic if it makes sense, but per-type scripts are easier to debug.


# 3.8 – Target Layout After Migration (Example)

After running your first wave of converters, your public repo should begin to look like this:

```text
/data/
  locations/
    loc_eldenhold_city.json
    loc_ashenvale_town.json
    ...
  npcs/
    npc_elyssa_dorne.json
    npc_dark_bronson.json
    ...
  factions/
    faction_merchants_guild.json
    ...
  stories/
    story_battle_of_the_bards.json
    ...
  sessions/
    session_S01.json
    session_S05.json
    ...

/site/pages/
  locations/
    eldenhold_city.md
    ashenvale_town.md
  npcs/
    elyssa_dorne.md
    dark_bronson.md
  stories/
    battle_of_the_bards.md
  sessions/
    session_S01.md
    session_S05.md
```

This confirms:
* JSON and Markdown are both in place.
* IDs and filenames follow the conventions.
* You have enough content to start building the site and AI prompts in later steps.


# 3.9 – Validate Migrated Data

After generating initial JSON:

1. Run the validator script (from Step 2’s “code AI” tools), which checks:
   * Required fields
   * Type correctness
   * ID shapes
   * Link integrity (e.g., `home_location_id` existing).

2. Manually spot-check:
   * Open a few JSON files.
   * Open the linked Markdown pages.
   * Confirm the lore looks right and is player-safe.

3. Fix issues in one of two places:
   * If the script logic is wrong → fix the script and re-run.
   * If the source data is weird → fix it in Notion or private files, re-export, then re-convert.

The goal is to end Step 3 with:
* A small but **clean** slice of the world in the public repo.


# 3.10 – “Done Enough” Criteria for Step 3

You do **not** need to migrate all of Sunspire to move on to Step 4.

Step 3 is “done enough” when:

* You have:
  * A handful of locations (especially major cities and starting regions).
  * A handful of key NPCs tied to those locations.
  * A few stories / vignettes tied to that slice.
  * A subset of session summaries that are already “canon” to the players.

* The data:
  * Follows your data model (Step 2).
  * Passes basic validation.
  * Lives in `/data` + `/site/pages` in the public repo.

At that point, you’re ready to:
* Build the **public site** around this foundation (Step 4).
* Let future expansions add more content over time.

----------------------------
----------------------------

# Step 4 – Build the Public-Facing Site & Connect the Map

**Goal:**  
Create a simple public Sunspire website that:
* Presents the world as a wiki-style lore site.
* Reads from the `/data` + `/site/pages` structure in your public repo.
* Links to (or embeds) the Sunspire Online interactive map.

This step is about:
* Information architecture (how pages are organized).
* Basic static site structure.
* Connecting the map to the site, even if it starts as a simple link.


# 4.2 – Choose a Static Site Approach

You want something:
* Simple
* Markdown-friendly
* GitHub Pages compatible

Reasonable options:
* Hand-rolled static site (HTML + CSS + light JS).
* A static site generator like:
  * MkDocs
  * Hugo
  * Jekyll

For now, assume:
* `/site` in the repo is the root of your public site content.
* GitHub Pages will serve from `/site` or from the repo root (depending on how you configure it).

You can refine the exact tool choice later with help from a coding-focused AI chat.


# 4.3 – Basic Site Folder Structure

In your public repo, flesh out `/site` like this:

```text
/site/
  index.html
  assets/
    css/
    js/
    images/
  pages/
    locations/
    npcs/
    factions/
    stories/
    sessions/
  map/
    (optional: helper page or embed for the interactive map)
```

Responsibilities:

* `index.html`
  * Main landing page for the site.
* `/assets`
  * CSS, JavaScript, global images.
* `/pages`
  * Markdown or HTML content grouped by type.
* `/map`
  * A page that either:
    * Embeds the interactive map, or
    * Links to where it’s hosted.


4.4 – Navigation & IA (Information Architecture)
Plan your main navigation with a few core sections:
⦁	Home
⦁	High-level intro to Sunspire.
⦁	Links to “Start Here” lore.
⦁	World
⦁	Regions / nations.
⦁	Major cities and locations.
⦁	People
⦁	NPCs grouped by region or role.
⦁	Optional PC section.
⦁	Factions
⦁	Organizations, cults, guilds.
⦁	Stories
⦁	Short stories, vignettes, in-world fiction.
⦁	Sessions
⦁	Episode-style recaps, in order.
⦁	Map
⦁	Link or embed for the interactive Sunspire map.
The goal is:
⦁	Easy for players to browse.
⦁	Easy for you to extend later as more data migrates.


# 4.5 – Binding JSON Data to Website Pages

You already decided in Step 2 that:
* JSON files live under `/data`
* Markdown pages live under `/site/pages`
* JSON points to Markdown via paths (e.g., `detail_markdown`, `text_markdown`, etc.)

For the site, you have two main patterns:

1. **Static generation (build-time)**
   * Run a script locally that:
     * Reads all JSON in `/data`.
     * Generates static HTML or Markdown pages into `/site/pages`.
   * Commit generated pages.

2. **Client-side loading (runtime)**
   * Have pages that:
     * Load JSON via JavaScript `fetch`.
     * Inject data into templates in the browser.

Short term:
* You can start with very simple static pages that are manually linked and filled.
* As you build tooling, you can move toward automatic generation.


# 4.6 – Hooking Up the Interactive Map

You already have the map engine and data in your `D:\Tracy\web` setup.

For the **public** repo and site, you have two main options:

1. **Link Only (Simple Option)**
   * Host the interactive map from your existing environment or from another repo/host.
   * Add a `map/index.html` page in `/site` that has:
     * Description of the map.
     * A big button or link: “Open Interactive Map”.

2. **Embed a Public-Safe Map Build**
   * Create a public-safe build of the map frontend.
     * Strip DM-only data.
     * Use only player-safe JSON.
   * Copy that into `/site/map` or a similar subfolder.
   * Adjust paths so map JS reads from `/data/locations` etc. (or from a packaged player build).

Starting with option (1) is perfectly fine:
* It gets the site and map logically connected.
* You can embed later once you have a stable content slice.


# 4.7 – GitHub Pages Setup (Conceptual)

High-level outline for enabling GitHub Pages:

1. Go to your public repo on GitHub.
2. Open **Settings → Pages**.
3. Choose source:
   * Either:
     * `main` branch, `/` root
     * or a `/docs` folder
     * or a `/site` folder (depending on how you structure it)
4. Save and wait for GitHub Pages to deploy.
5. You will get a URL like:
   * `https://<username>.github.io/sunspire-online-public/`

Your job in Step 4 is to:
* Ensure your main `index.html` and `/site` content line up with the Pages configuration.
* Confirm that links, images, and `/pages` URLs work on the live site.


# 4.8 – Minimum Viable Site

For Step 4, you do **not** need a finished, pretty, fully-populated site.

The minimum bar:

* Home page (`index.html`) that:
  * Introduces Sunspire.
  * Links to at least:
    * One location page.
    * One NPC.
    * One story or session.
    * The Map page or link.

* At least:
  * A handful of pages under `/site/pages/locations`, `/site/pages/npcs`, etc.
    * These should correspond to migrated JSON entities from Step 3.

* GitHub Pages live and serving:
  * Confirm your site loads at the GitHub Pages URL.

At that point, you have a **real**, public-facing Sunspire presence.


# 4.9 – What to Ask the “Code AI” Chat For

When you’re ready to automate pieces of Step 4, a coding-oriented chat can help with:

1. **Basic static site skeleton**
   * Generate:
     * `index.html`
     * A simple layout template
     * Navigation bar
     * A few starter pages in `/site/pages`

2. **Data-driven page generation**
   * A script that:
     * Reads `/data/locations/*.json`
     * Creates or updates corresponding pages in `/site/pages/locations`
     * Inserts summary and links.

3. **Map link or embed page**
   * An HTML page under `/site/map/` that:
     * Either embeds an iframe with the interactive map.
     * Or offers a clear “Open Map” button to an external map URL.

4. **GitHub Pages config assistance**
   * Help creating:
     * The correct folder structure for Pages.
     * A `CNAME` file if you ever decide to use a custom domain.

You don’t need all of this immediately, but having it written down keeps Step 4 focused and finite.

---

**Step 4 is “done” when:**
* GitHub Pages is enabled and serving your site.
* The site reads from data migrated in Step 3.
* The site includes:
  * Home page
  * A few working lore pages (locations/NPCs/stories/sessions)
  * A Map link or embed

----------------------------
----------------------------

# Step 5 – Design the AI Generation Pipeline

**Goal:**  
Define how an AI “worker” will:
* Read lore from the public repo (`/data`, `/site/pages`).
* Generate new stories, vignettes, flavor text, and NPC interactions.
* Save results in a consistent, reviewable way.

This step is **design-only**:
* No actual model wiring here yet.
* You define folders, task types, and expectations.
* Another chat can later turn this into real scripts.


# 5.2 – Concept: AI as a Lore Worker

Think of the AI not as “the DM” but as:
* A lore assistant.
* A writer’s room intern.
* A generator of raw material you approve or reject.

The pipeline should:
1. Pull the latest repo data (or read a local clone).
2. Identify **targets** (NPCs/locations/stories that need content).
3. Build **structured prompts** from JSON + Markdown.
4. Call the AI model.
5. Save **draft outputs** into a controlled folder.
6. Only after your review, promote content into `/data` + `/site/pages`.

The pipeline should **not**:
* Directly overwrite your canon JSON.
* Introduce facts that contradict established lore, if you can help it.


# 5.3 – AI-Related Folders in the Public Repo

Under your public repo, you already reserved `/ai`.  
Let’s give it a more concrete structure:

```text
/ai/
  configs/
  prompts/
  work_queue/
  output/
```

**Roles:**

* `/ai/configs/`
  * JSON config files that define task types, parameters, and preferences.

* `/ai/prompts/`
  * Prompt templates, one per task type (or more, if needed).

* `/ai/work_queue/`
  * Files that describe what needs to be generated (tasks).

* `/ai/output/`
  * Raw AI outputs: JSON + Markdown bundles.
  * These are drafts, not canon.


# 5.4 – Task Types

Don’t build “one mega-task that does everything.”  
Define small, targeted task types.

Examples:

1. `generate_npc_vignette`
   * Input:
     * NPC ID
     * Home location ID
     * Optional: time context (before/after session X)
   * Output:
     * A `story` JSON + Markdown describing a short scene.

2. `generate_location_flavor`
   * Input:
     * Location ID
   * Output:
     * Extra descriptive text to extend `detail_markdown`.

3. `generate_npc_relationships`
   * Input:
     * A group of NPC IDs in a shared location or faction.
   * Output:
     * Relationship descriptions and potential story hooks.

4. `generate_session_gap_scene`
   * Input:
     * Session ID
   * Output:
     * One or more small scenes that occur off-screen between sessions.

Each task type gets:
* A config file under `/ai/configs`.
* One or more prompt templates under `/ai/prompts`.


# 5.5 – Prompt Structure (Conceptual)

A good prompt for your use case has:

1. **System / role instructions**  
   e.g., “You are a lore writer for the Sunspire campaign. Stay consistent with provided data. Do not contradict or overwrite canon. Keep tone grounded, dark-fantasy, with occasional humor.”

2. **Lore context bundle**
   * JSON for:
     * The core entity (NPC, location, etc.)
     * Related entities (location, faction, key NPCs)
   * Markdown excerpts:
     * Backstory
     * Scenes
     * Session summaries

3. **Instructions for this specific task**
   * “Generate a 500–800 word vignette set in X.”
   * “Focus on the relationship between A and B.”
   * “This scene happens shortly before Session S05, but players haven’t seen it.”

4. **Output format**
   * Either:
     * “Return only Markdown for the story.”
     * Or:
     * “Return a JSON + Markdown pair in this exact structure.”

These templates live in `/ai/prompts` so scripts can load them.


# 5.6 – Work Queue Task Files

To avoid hardcoding everything in scripts, use **task files** placed in `/ai/work_queue`.

Example: `/ai/work_queue/task_001_generate_npc_vignette.json`

```json
{
  "task_id": "task_001_generate_npc_vignette",
  "type": "generate_npc_vignette",
  "npc_id": "npc_elyssa_dorne",
  "primary_location_id": "loc_eldenhold_city",
  "timeline": {
    "relative_to_session": "S05",
    "when": "before"
  },
  "output_slug": "story_elyssa_whispers_before_S05"
}
```

The AI runner script will:
* Look at `/ai/work_queue/*.json`.
* For each:
  * Load the task.
  * Gather context from `/data` + `/site/pages`.
  * Load the appropriate prompt.
  * Call the AI model.
  * Save output under `/ai/output/<task_id>/...`.

Once you review and approve output, a separate step will promote it into `/data/stories` and `/site/pages/stories`.


# 5.7 – Output Format & Drafts

For each task, the AI runner should create a small folder under `/ai/output`, like:

```text
/ai/output/task_001_generate_npc_vignette/
  story.json
  story.md
  metadata.json
```

Where:
* `story.json` – new `story` JSON that matches your data model.
* `story.md` – the markdown text of the vignette.
* `metadata.json` – info like:
  * `task_id`
  * `generated_at`
  * `model_used`
  * `source_context` (optional)

This keeps drafts:
* Separate from canon.
* Organized by task.
* Easy to review.


# 5.8 – Human-in-the-Loop Review

You want **control** over what becomes canon.

Recommended flow:

1. Run the AI worker on a batch of tasks.
2. Open `/ai/output` and read:
   * `story.md`
   * Or equivalent output for other task types.
3. For each output:
   * **Approve**:
     * Copy or move the JSON/Markdown into proper locations:
       * `story.json` → `/data/stories`
       * `story.md` → `/site/pages/stories`
     * Update related entities (e.g., add `story_hook_ids` to NPCs).
   * **Reject**:
     * Delete the task’s output folder.
     * Optionally write notes for why, for future prompt tuning.

Over time, you can semi-automate the “promote to canon” step, but keep a manual gate at first.


# 5.9 – Where the AI Pipeline Runs

Likely place: **your local machine** (PC or TracyPi environment).

Typical flow:

1. Pull latest public repo:
   * `git pull` in your local public repo clone.

2. Run AI runner script:
   * It:
     * Reads `/ai/work_queue`.
     * Reads `/data` + `/site/pages`.
     * Calls local model or API.
     * Writes to `/ai/output`.

3. Review & promote approved outputs into `/data` + `/site/pages`.

4. Commit and push:
   * `git add .`
   * `git commit`
   * `git push`

You **do not** need to run this pipeline on every commit.  
Treat it like a tool you use when you want to bulk-generate lore.


# 5.10 – What to Ask the “Code AI” Chat For

When you’re ready to build the actual AI runner code, you can ask another chat to:

1. **Write a task runner script** (e.g., `run_ai_tasks.py`):
   * Reads all `/ai/work_queue/*.json`.
   * For each task:
     * Loads relevant JSON entities from `/data`.
     * Loads prompt template from `/ai/prompts`.
     * Builds a prompt by injecting JSON + Markdown context.
     * Sends the prompt to:
       * Your local model (via API or CLI), or
       * A remote API (if you choose to use one).
     * Saves output into `/ai/output/<task_id>/...`.

2. **Create helper utilities**:
   * A script to generate tasks automatically:
     * Example: “Create `generate_npc_vignette` tasks for every NPC without any `story_hook_ids`.”
   * A script to promote approved `/ai/output` results into `/data` + `/site/pages`.

3. **Add logging and safety checks**:
   * Ensure nothing directly overwrites existing JSON without explicit intention.
   * Optionally require a flag or “dry run” mode for tests.

---

**Step 5 is “done” when:**
* `/ai/configs`, `/ai/prompts`, `/ai/work_queue`, `/ai/output` are defined and documented.
* At least one task type (e.g., `generate_npc_vignette`) is fully thought through:
  * What it consumes.
  * What it outputs.
  * Where drafts live.
* You have a clear requests list for the coding chat to implement the runner.

----------------------------
----------------------------

# 6 – Checklist for Updating / Adding Lore

Whenever you add or change an entity (location, NPC, story, etc.), run through this quick checklist:

1. **Is this player-safe?**
   * If not, keep it private only.
   * If partially safe, write a redacted version for the public repo.

2. **Does it have a stable ID?**
   * Use your naming convention:
     * `loc_...`, `npc_...`, `story_...`, `session_...`, etc.

3. **Are relationships defined?**
   * Locations:
     * Region, factions, key NPCs.
   * NPCs:
     * Home location, relevant factions.
   * Stories:
     * Participants, primary location, timeline hints.

4. **Are tags present and sensible?**
   * Theme tags (`political_intrigue`, `cosmic_horror`, etc.).
   * Role tags (`intro_hook`, `downtime_scene`, etc.).

5. **Does Markdown exist where referenced?**
   * If JSON points to a Markdown file, make sure the file is actually there.

6. **Validate**
   * Run the validator and fix any issues before you push.
