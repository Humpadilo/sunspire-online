import json
from pathlib import Path

ROOT = Path(r"D:\SunspireOnlinePublic")
LOC_DIR = ROOT / "data" / "locations"

ALLOWED_CATEGORIES = {"world", "nation", "region", "city", "site"}


def load_all_locations():
    """
    Load all location objects from data/locations/*.json
    Returns (locations_by_id, all_locations, errors)
    """
    locations_by_id = {}
    all_locations = []
    errors = []

    for path in sorted(LOC_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"[FATAL] {path.name}: invalid JSON: {e}")
            continue

        if isinstance(data, dict) and "locations" in data:
            arr = data["locations"]
        elif isinstance(data, list):
            arr = data
        else:
            errors.append(f"[WARN] {path.name}: unexpected root type (expected list or {{'locations':[]}})")
            continue

        if not isinstance(arr, list):
            errors.append(f"[WARN] {path.name}: locations root is not a list")
            continue

        for obj in arr:
            if not isinstance(obj, dict):
                continue
            obj["_file"] = path.name
            all_locations.append(obj)
            loc_id = obj.get("id")
            if loc_id:
                if loc_id in locations_by_id:
                    existing_file = locations_by_id[loc_id].get("_file")
                    # Allow duplicates when one copy is in world_nations.json
                    if not (
                        path.name == "world_nations.json"
                        or existing_file == "world_nations.json"
                    ):
                        errors.append(
                            f"[ERROR] {path.name}: duplicate id {loc_id!r} "
                            f"(also in {existing_file})"
                        )
                    # Do NOT overwrite the first-seen version in locations_by_id
                else:
                    locations_by_id[loc_id] = obj

    return locations_by_id, all_locations, errors


def validate_locations():
    locations_by_id, all_locations, errors = load_all_locations()

    for obj in all_locations:
        file = obj.get("_file", "<unknown>")
        loc_id = obj.get("id")
        cat = obj.get("category")
        loc_type = obj.get("type")
        region = obj.get("region")
        map_id = obj.get("map_id")
        parent = obj.get("parent_location_id")

        # Basic required fields
        if not loc_id:
            name = obj.get("NameEntity_Name") or obj.get("name")
            errors.append(f"[ERROR] {file}: location missing 'id' (NameEntity_Name={name!r})")

        if loc_type != "location":
            errors.append(f"[ERROR] {file}: id={loc_id!r} has type={loc_type!r} (expected 'location')")

        if not cat:
            errors.append(f"[ERROR] {file}: id={loc_id!r} missing 'category'")
        elif cat not in ALLOWED_CATEGORIES:
            errors.append(
                f"[ERROR] {file}: id={loc_id!r} has invalid category={cat!r} "
                f"(allowed: {sorted(ALLOWED_CATEGORIES)})"
            )

        if not region:
            errors.append(f"[WARN] {file}: id={loc_id!r} missing 'region'")

        if not map_id:
            errors.append(f"[WARN] {file}: id={loc_id!r} missing 'map_id'")

        # Parent existence check
        if parent and parent not in locations_by_id:
            errors.append(
                f"[ERROR] {file}: id={loc_id!r} has parent_location_id={parent!r} "
                f"which does not exist in any location file"
            )

    return errors


def main():
    errors = validate_locations()
    if not errors:
        print("All locations look valid.")
        return

    fatal = [e for e in errors if e.startswith("[FATAL]")]
    err = [e for e in errors if e.startswith("[ERROR]")]
    warn = [e for e in errors if e.startswith("[WARN]")]

    if fatal:
        print("=== FATAL ===")
        for e in fatal:
            print(e)
        print()

    if err:
        print("=== ERRORS ===")
        for e in err:
            print(e)
        print()

    if warn:
        print("=== WARNINGS ===")
        for e in warn:
            print(e)
        print()

    print(f"Summary: {len(fatal)} fatal, {len(err)} errors, {len(warn)} warnings.")


if __name__ == "__main__":
    main()
