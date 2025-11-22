import json
import re
from pathlib import Path

ROOT = Path(r"D:\SunspireOnlinePublic")
VALERIA_PATH = ROOT / "data" / "locations" / "valeria_locations.json"
MIREHOLM_PATH = ROOT / "data" / "locations" / "mireholm_locations.json"


def slugify(name: str) -> str:
    """
    Turn a building/site name into a lowercase_slug for IDs.
    Examples:
      "The Broken Dagger" -> "broken_dagger"
      "Valeria Castle"    -> "valeria_castle"
    """
    if not name:
        return "unnamed_site"
    s = name.strip()
    # Strip leading "The "
    if s.lower().startswith("the "):
        s = s[4:]
    # Normalize whitespace
    s = re.sub(r"\s+", " ", s)
    # Replace non-alphanumeric with underscores
    s = re.sub(r"[^a-zA-Z0-9]+", "_", s)
    s = s.strip("_").lower()
    return s or "unnamed_site"


def promote_sites_in_file(path: Path, parent_id: str, parent_region: str):
    """
    For the given locations file, find any objects WITHOUT an 'id'
    and promote them to proper 'site' locations under the given parent.
    """
    if not path.exists():
        print(f"[SKIP] {path} does not exist")
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
        print(f"[WARN] {path.name}: unexpected JSON root (expected list or {{'locations': []}})")
        return

    if not isinstance(arr, list):
        print(f"[WARN] {path.name}: locations root is not a list")
        return

    # Infer a parent slug from the parent_id: e.g. "loc_eldenhold_city" -> "eldenhold"
    parent_slug = parent_id
    if parent_id.startswith("loc_"):
        parent_slug = parent_id[4:]
    # Drop trailing "_city" / "_region" / "_nation" / "_site" if present
    for suffix in ("_city", "_region", "_nation", "_site"):
        if parent_slug.endswith(suffix):
            parent_slug = parent_slug[: -len(suffix)]

    new_arr = []
    promoted_count = 0

    for obj in arr:
        if not isinstance(obj, dict):
            new_arr.append(obj)
            continue

        # If it already has an id, it's a nation/city/region we've already normalized.
        if "id" in obj:
            new_arr.append(obj)
            continue

        raw_name = (
            obj.get("NameEntity_Name")
            or obj.get("name")
            or obj.get("Name")
            or obj.get("title")
        )

        site_slug = slugify(raw_name or "")
        loc_id = f"loc_{parent_slug}_{site_slug}_site"

        # Build a new object starting from the original so we keep legacy fields
        new_obj = dict(obj)

        # Core fields for a site
        new_obj["id"] = loc_id
        new_obj["type"] = "location"
        new_obj["name"] = raw_name or "Unnamed Site"

        # Aliases: if there was a previous name field that differs, keep it
        aliases = set()
        prev_aliases = obj.get("aliases")
        if isinstance(prev_aliases, list):
            for a in prev_aliases:
                if a:
                    aliases.add(str(a))
        # We don't try to get fancy here; raw_name is already the main name
        new_obj["aliases"] = sorted(aliases)

        new_obj["category"] = "site"
        new_obj["region"] = parent_region
        new_obj["parent_location_id"] = parent_id

        # Map ID: try to use the original Map field if present, otherwise fall back to "Sunspire"
        map_id = obj.get("Map") or obj.get("map_id") or "Sunspire"
        new_obj["map_id"] = map_id

        # Tags: add site + player_safe, and preserve any previous list
        tags = {"site", "player_safe"}
        prev_tags = obj.get("tags")
        if isinstance(prev_tags, list):
            for t in prev_tags:
                if t:
                    tags.add(str(t))
        new_obj["tags"] = sorted(tags)

        # Summary / detail path
        summary = obj.get("Description") or obj.get("summary") or ""
        new_obj.setdefault("summary", summary)

        # Simple default markdown path based on ID
        markdown_name = loc_id.replace("loc_", "")
        new_obj.setdefault("detail_markdown", f"site/pages/locations/{markdown_name}.md")

        # Ensure link fields exist
        new_obj.setdefault("faction_ids", [])
        new_obj.setdefault("related_npc_ids", [])
        new_obj.setdefault("story_ids", [])
        new_obj.setdefault("session_ids", [])
        new_obj.setdefault("first_mentioned_session", None)
        new_obj.setdefault("source_refs", [])

        new_arr.append(new_obj)
        promoted_count += 1

    if container_is_dict:
        data["locations"] = new_arr
    else:
        data = new_arr

    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[OK] Promoted {promoted_count} site(s) in {path.name}")


def main():
    # All buildings in valeria_locations.json belong to Eldenhold
    promote_sites_in_file(
        VALERIA_PATH,
        parent_id="loc_eldenhold_city",
        parent_region="Valeria",
    )

    # All buildings in mireholm_locations.json belong to Gravenhollow
    promote_sites_in_file(
        MIREHOLM_PATH,
        parent_id="loc_gravenhollow_city",
        parent_region="Mireholm",
    )


if __name__ == "__main__":
    main()
