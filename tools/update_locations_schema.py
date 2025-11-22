import json
from pathlib import Path

# Root of the public repo
ROOT = Path(r"D:\SunspireOnlinePublic")

# Location files we want to process in this batch.
# Adjust this list as needed.
LOCATION_FILES = [
    ROOT / "data" / "locations" / "world_nations.json",
    ROOT / "data" / "locations" / "valeria_locations.json",
    ROOT / "data" / "locations" / "mireholm_locations.json",
    ROOT / "data" / "locations" / "sylvara_locations.json",
    ROOT / "data" / "locations" / "deadlands_locations.json",
    ROOT / "data" / "locations" / "greenhollow_locations.json",
    ROOT / "data" / "locations" / "karak_thul_locations.json",
    ROOT / "data" / "locations" / "skraggmar_locations.json",
    ROOT / "data" / "locations" / "thra_zul_locations.json",
    ROOT / "data" / "locations" / "xorath_kul_locations.json",
    ROOT / "data" / "locations" / "big_titty_demon_island.json",
]

# Canonical config from docs/world_hierarchy.md
# Each entry keyed by canonical ID.
CANONICAL_LOCATIONS = {
    # World
    "loc_sunspire_world": {
        "name": "Sunspire",
        "aliases": [],
        "category": "world",
        "region": None,
        "parent": None,
        "map_id": "Sunspire",
        "tags": ["world", "player_safe"],
    },
    # Nations
    "loc_valeria_nation": {
        "name": "Valeria",
        "aliases": ["Valeris", "Valerian"],
        "category": "nation",
        "region": "Sunspire World",
        "parent": "loc_sunspire_world",
        "map_id": "Sunspire",
        "tags": ["nation", "player_safe"],
    },
    "loc_mireholm_nation": {
        "name": "Mireholm",
        "aliases": [],
        "category": "nation",
        "region": "Sunspire World",
        "parent": "loc_sunspire_world",
        "map_id": "Sunspire",
        "tags": ["nation", "player_safe"],
    },
    "loc_sylvara_nation": {
        "name": "Sylvara",
        "aliases": ["Sylvara: The Elven Forests"],
        "category": "nation",
        "region": "Sunspire World",
        "parent": "loc_sunspire_world",
        "map_id": "Sunspire",
        "tags": ["nation", "player_safe"],
    },
    "loc_deadlands_nation": {
        "name": "Deadlands",
        "aliases": [],
        "category": "nation",
        "region": "Sunspire World",
        "parent": "loc_sunspire_world",
        "map_id": "Sunspire",
        "tags": ["nation", "player_safe"],
    },
    "loc_greenhollow_nation": {
        "name": "Greenhollow",
        "aliases": [],
        "category": "nation",
        "region": "Sunspire World",
        "parent": "loc_sunspire_world",
        "map_id": "Sunspire",
        "tags": ["nation", "player_safe"],
    },
    "loc_karak_thul_nation": {
        "name": "Karak Thul",
        "aliases": [
            "Karak-Thul",
            "Karak Thûl",
            "Karak Thûl: The Dwarven Mountains",
        ],
        "category": "nation",
        "region": "Sunspire World",
        "parent": "loc_sunspire_world",
        "map_id": "Sunspire",
        "tags": ["nation", "player_safe"],
    },
    "loc_skraggmar_nation": {
        "name": "Skraggmar",
        "aliases": [],
        "category": "nation",
        "region": "Sunspire World",
        "parent": "loc_sunspire_world",
        "map_id": "Sunspire",
        "tags": ["nation", "player_safe"],
    },
    "loc_thra_zul_nation": {
        "name": "Thra Zul",
        "aliases": [
            "Thrazul",
            "Thra-Zul",
            "Thra’Zul",
            "Thra’Zul: The Orcish Badlands",
            "Thrazhul",
            "Thra-Zhul",
            "Thra’Zhul",
            "Thra’Zhul: The Orcish Badlands",            
        ],
        "category": "nation",
        "region": "Sunspire World",
        "parent": "loc_sunspire_world",
        "map_id": "Sunspire",
        "tags": ["nation", "player_safe"],
    },
    "loc_xorath_kul_nation": {
        "name": "Xorath Kul",
        "aliases": [
            "Xorath-Kul",
            "Xorath’Kul",
            "Xorath’Kul: The Underdark",
        ],
        "category": "nation",
        "region": "Sunspire World",
        "parent": "loc_sunspire_world",
        "map_id": "Sunspire",
        "tags": ["nation", "player_safe"],
    },
    # BTDI region + children
    "loc_big_titty_demon_island_region": {
        "name": "Big Titty Demon Island",
        "aliases": ["Big Tiddy Deamon Island", "Big Titty Island"],
        "category": "region",
        "region": "Sunspire World",
        "parent": "loc_sunspire_world",
        "map_id": "Sunspire",
        "tags": ["region", "island", "player_safe"],
    },
    "loc_big_titty_island_coast_region": {
        "name": "Big Titty Island Coast",
        "aliases": [],
        "category": "region",
        "region": "Big Titty Demon Island",
        "parent": "loc_big_titty_demon_island_region",
        "map_id": "Big Tiddy Deamon Island",
        "tags": ["region", "coast", "player_safe"],
    },
    "loc_crystal_hinge_site": {
        "name": "Crystal Hinge",
        "aliases": [],
        "category": "site",
        "region": "Big Titty Demon Island",
        "parent": "loc_big_titty_demon_island_region",
        "map_id": "Big Tiddy Deamon Island",
        "tags": ["site", "player_safe"],
    },
    # Cities (we'll normalize these in their files later)
    "loc_eldenhold_city": {
        "name": "Eldenhold",
        "aliases": [],
        "category": "city",
        "region": "Valeria",
        "parent": "loc_valeria_nation",
        "map_id": "Sunspire",
        "tags": ["city", "player_safe"],
    },
    "loc_ashenvale_city": {
        "name": "Ashenvale",
        "aliases": [],
        "category": "city",
        "region": "Valeria",
        "parent": "loc_valeria_nation",
        "map_id": "Sunspire",
        "tags": ["city", "player_safe"],
    },
    "loc_port_town_city": {
        "name": "Port Town",
        "aliases": ["Pot Town"],
        "category": "city",
        "region": "Valeria",
        "parent": "loc_valeria_nation",
        "map_id": "Sunspire",
        "tags": ["city", "player_safe"],
    },
    "loc_gravenhollow_city": {
        "name": "Gravenhollow",
        "aliases": [],
        "category": "city",
        "region": "Mireholm",
        "parent": "loc_mireholm_nation",
        "map_id": "Sunspire",
        "tags": ["city", "player_safe"],
    },
}

# Reverse lookup map: normalized name -> list of candidate canonical IDs
NAME_INDEX = {}

def build_name_index():
    def norm(s: str) -> str:
        return s.lower().strip()

    for cid, meta in CANONICAL_LOCATIONS.items():
        all_names = [meta["name"]] + meta.get("aliases", [])
        for raw in all_names:
            key = norm(raw.split(":")[0])  # strip stuff after colon, e.g. "Sylvara: The Elven Forests"
            NAME_INDEX.setdefault(key, set()).add(cid)


def guess_canonical_id(raw_name: str):
    if not raw_name:
        return None
    base = raw_name.split(":")[0]
    key = base.lower().strip()
    candidates = NAME_INDEX.get(key)
    if not candidates:
        return None
    if len(candidates) == 1:
        return next(iter(candidates))
    # If ambiguous, just bail for now
    return None


def normalize_location_obj(obj: dict, file_path: Path) -> dict:
    """
    Given a raw location object, normalize it to the new schema
    while preserving all original keys.
    """

    # Try several fields to get a human-readable name to match on
    raw_name = (
        obj.get("NameEntity_Name")
        or obj.get("name")
        or obj.get("Name")
        or obj.get("title")
    )

    cid = obj.get("id")
    if cid and cid in CANONICAL_LOCATIONS:
        canonical_id = cid
    else:
        canonical_id = guess_canonical_id(raw_name)

    if not canonical_id:
        print(f"[WARN] Could not resolve canonical ID for location in {file_path.name}: {raw_name!r}")
        return obj  # leave as-is

    meta = CANONICAL_LOCATIONS[canonical_id]

    # Start with a shallow copy so we don't mutate in-place
    new_obj = dict(obj)

    # Core fields
    new_obj["id"] = canonical_id
    new_obj["type"] = "location"
    new_obj["name"] = meta["name"]

    # Aliases: merge canonical aliases + any old variants (if present)
    aliases = set(meta.get("aliases", []))

    # Include the old NameEntity_Name if it's not the same as canonical name
    if raw_name and raw_name != meta["name"]:
        aliases.add(raw_name)

    # Include previous aliases field if present
    prev_aliases = obj.get("aliases")
    if isinstance(prev_aliases, list):
        for a in prev_aliases:
            aliases.add(a)

    new_obj["aliases"] = sorted(a for a in aliases if a)

    # Category, region, parent, map
    new_obj["category"] = meta["category"]
    new_obj["region"] = meta["region"] or "Sunspire World"
    new_obj["parent_location_id"] = meta["parent"]
    new_obj["map_id"] = meta["map_id"]

    # Tags: merge canonical + any existing tags array
    tags = set(meta.get("tags", []))
    prev_tags = obj.get("tags")
    if isinstance(prev_tags, list):
        for t in prev_tags:
            tags.add(str(t))
    new_obj["tags"] = sorted(tags)

    # Ensure link fields exist
    new_obj.setdefault("summary", obj.get("Description") or "")
    new_obj.setdefault("detail_markdown", "")
    new_obj.setdefault("faction_ids", [])
    new_obj.setdefault("related_npc_ids", [])
    new_obj.setdefault("story_ids", [])
    new_obj.setdefault("session_ids", [])
    new_obj.setdefault("first_mentioned_session", None)
    new_obj.setdefault("source_refs", [])

    return new_obj


def process_file(path: Path):
    if not path.exists():
        print(f"[SKIP] File not found: {path}")
        return

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[ERROR] Failed to load JSON from {path}: {e}")
        return

    if isinstance(data, dict) and "locations" in data:
        arr = data["locations"]
        container_is_dict = True
    elif isinstance(data, list):
        arr = data
        container_is_dict = False
    else:
        print(f"[WARN] Unexpected JSON root in {path} (expected list or {{'locations':[]}})")
        return

    if not isinstance(arr, list):
        print(f"[WARN] Locations root is not a list in {path}")
        return

    new_arr = []
    for obj in arr:
        if not isinstance(obj, dict):
            new_arr.append(obj)
            continue
        new_arr.append(normalize_location_obj(obj, path))

    if container_is_dict:
        data["locations"] = new_arr
    else:
        data = new_arr

    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[OK] Updated {path}")


def main():
    build_name_index()
    for path in LOCATION_FILES:
        process_file(path)


if __name__ == "__main__":
    main()
