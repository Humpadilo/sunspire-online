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


# 1.6 – Add Roadmap & Step Files to `/docs/roadmap`

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
