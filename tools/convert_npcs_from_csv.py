import csv
import json
import os
import re
from pathlib import Path

REPO_ROOT = Path(r"D:\SunspireOnlinePublic")

CSV_PATH = REPO_ROOT / "import_queue" / "npcs" / "valeria_eldenhold" / "Eldenhold_NPC.csv"
OUT_JSON_DIR = REPO_ROOT / "data" / "npcs"
OUT_MD_DIR   = REPO_ROOT / "site" / "pages" / "npcs"

# ---- User-editable location mapping ----
# Add/adjust mappings if you want finer homes than just "Eldenhold batch".
LOCATION_ID_MAP = {
    "eldenhold": "loc_eldenhold_city",
    "gravenhollow": "loc_gravenhollow_city",
    "valeria": "loc_valeria_nation",
    "mireholm": "loc_mireholm_nation",
    "btdi": "loc_big_titty_demon_island_region",
    "big titty": "loc_big_titty_demon_island_region",
}

def slugify(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s

def parse_tags(tag_str: str):
    if not tag_str:
        return []
    parts = re.split(r"[;,]", tag_str)
    return [p.strip().lower() for p in parts if p.strip()]

def map_home_location(loc_str: str):
    if not loc_str:
        return "loc_eldenhold_city"  # default for this CSV batch
    s = loc_str.lower()
    for key, loc_id in LOCATION_ID_MAP.items():
        if key in s:
            return loc_id
    # fallback for Eldenhold CSV
    return "loc_eldenhold_city"

def parse_race_gender(race_field: str):
    race = None
    gender = None
    if not race_field:
        return race, gender
    parts = [p.strip() for p in race_field.split(",") if p.strip()]
    if len(parts) == 1:
        race = parts[0]
    elif len(parts) >= 2:
        race = parts[0]
        gender = parts[1].lower()
    return race, gender

def first_sentence(text: str, max_len=220):
    if not text:
        return ""
    t = " ".join(text.split())
    if len(t) <= max_len:
        return t
    # try to cut at first period within limit
    cut = t[:max_len]
    if "." in cut:
        return cut.split(".")[0].strip() + "."
    return cut.strip() + "..."

def main(overwrite=False):
    OUT_JSON_DIR.mkdir(parents=True, exist_ok=True)
    OUT_MD_DIR.mkdir(parents=True, exist_ok=True)

    with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    created = 0
    skipped = 0

    for row in rows:
        name = (row.get("Name") or "").strip()
        if not name:
            continue

        slug = slugify(name)
        npc_id = f"npc_{slug}"

        status = (row.get("Status") or "").strip().lower() or None
        location_str = (row.get("Location") or "").strip()
        tags_csv = parse_tags((row.get("Tags") or "").strip())

        background = (row.get("Background Story") or "").strip()
        notes = (row.get("Notes") or "").strip()
        appearance = (row.get("Appearance") or "").strip()
        cls = (row.get("Class") or "").strip()
        faction = (row.get("Faction") or "").strip()
        role = (row.get("Role") or "").strip()

        race_field = (row.get("Race") or "").strip()
        race, gender = parse_race_gender(race_field)

        home_location_id = map_home_location(location_str)

        # image handling: keep basename, assume you’ll move it to site/assets/images/npcs/
        image_raw = (row.get("Image") or "").strip()
        image_basename = os.path.basename(image_raw) if image_raw else ""
        image_path = f"site/assets/images/npcs/{image_basename}" if image_basename else None

        # tags: csv tags + race + location hint + player_safe
        tags = []
        tags.extend(tags_csv)
        if race:
            tags.append(race.lower())
        if "eldenhold" in location_str.lower():
            tags.append("eldenhold")
        if "btdi" in location_str.lower() or "big titty" in location_str.lower():
            tags.append("btdi")
        tags.append("player_safe")
        # de-dupe while preserving order
        seen = set()
        tags = [t for t in tags if not (t in seen or seen.add(t))]

        public_summary = first_sentence(background or notes)

        npc_json = {
            "id": npc_id,
            "type": "npc",
            "name": name,
            "role": role or None,
            "status": status,
            "race": race,
            "gender": gender,
            "home_location_id": home_location_id,
            "tags": tags,
            "public_summary": public_summary,
            "backstory_markdown": f"site/pages/npcs/{slug}.md",
            "faction_ids": [],
            "story_hook_ids": [],
            "related_npc_ids": [],
            "image_path": image_path,
            "source_refs": [
                {"kind": "import_queue_csv", "ref": str(CSV_PATH.relative_to(REPO_ROOT)).replace("\\", "/")}
            ],
        }

        # remove None fields to keep output clean
        npc_json = {k: v for k, v in npc_json.items() if v is not None}

        json_path = OUT_JSON_DIR / f"{npc_id}.json"
        md_path = OUT_MD_DIR / f"{slug}.md"

        if json_path.exists() and not overwrite:
            skipped += 1
            continue

        with open(json_path, "w", encoding="utf-8") as jf:
            json.dump(npc_json, jf, indent=2, ensure_ascii=False)

        md_lines = [
            f"# {name}",
            "",
        ]
        if background:
            md_lines.append(background)
            md_lines.append("")
        if notes:
            md_lines.append("## Notes")
            md_lines.append(notes)
            md_lines.append("")
        if appearance:
            md_lines.append("## Appearance")
            md_lines.append(appearance)
            md_lines.append("")
        if cls:
            md_lines.append("## Class")
            md_lines.append(cls)
            md_lines.append("")
        if faction:
            md_lines.append("## Faction")
            md_lines.append(faction)
            md_lines.append("")

        with open(md_path, "w", encoding="utf-8") as mf:
            mf.write("\n".join(md_lines).strip() + "\n")

        created += 1

    print(f"[OK] NPC conversion complete. Created/updated: {created}, skipped (already existed): {skipped}")
    print(f"[INFO] JSON out: {OUT_JSON_DIR}")
    print(f"[INFO] MD out:   {OUT_MD_DIR}")

if __name__ == "__main__":
    # overwrite=False by default. Set True if you want to regenerate everything.
    main(overwrite=False)
