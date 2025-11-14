# Sunspire World – Location Hierarchy (Canonical)

This file is the **source of truth** for world / nation / city / sub-location naming.

Use these names and IDs in:

- `data/locations/*.json`
- Map config & markers
- Any future scripts or AI prompts

---

## 1. Tree View (World → Nations → Cities → Sub-locations)

**World**

- **Sunspire** (world)  
  - **Valeria** (nation)  
    - **Eldenhold** (city)  
      - [multiple building / site locations]  
    - **Ashenvale** (city)  
    - **Port Town** (city)  
      - [multiple building / site locations]  
  - **Mireholm** (nation)  
    - **Gravenhollow** (city)  
      - [multiple building / site locations]  
  - **Big Titty Demon Island** (region)  
    - **Big Titty Island Coast** (region)  
    - **Crystal Hinge** (site)  
  - **Sylvara** (nation)  
  - **Deadlands** (nation)  
  - **Greenhollow** (nation)  
  - **Karak Thul** (nation)  
  - **Skraggmar** (nation)  
  - **Thra Zhul** (nation)  
  - **Xorath Kul** (nation)  

Notes:

- “Big Titty Demon Island” is treated as a **region / island**, not a nation.
- Nations without cities listed here simply don’t have defined sub-areas *yet*.

---

## 2. Canonical IDs & Names

These are the canonical IDs and display names for use in JSON.

### 2.1 World

| ID                  | Name      | Category | Parent ID           | Notes |
|---------------------|-----------|----------|---------------------|-------|
| `loc_sunspire_world` | Sunspire | world    | `null`              | Top-level world container |

### 2.2 Nations & Regions

| ID                       | Name                    | Category | Parent ID           | Known variants / typos               |
|--------------------------|-------------------------|----------|---------------------|--------------------------------------|
| `loc_valeria_nation`     | Valeria                 | nation   | `loc_sunspire_world` (eventual) | “Valeris” (legacy), “Valerian” (legacy) |
| `loc_mireholm_nation`    | Mireholm                | nation   | `loc_sunspire_world` (eventual) | – |
| `loc_sylvara_nation`     | Sylvara                 | nation   | `loc_sunspire_world` (eventual) | “Sylvara: The Elven Forests” (extended title) |
| `loc_deadlands_nation`   | Deadlands               | nation   | `loc_sunspire_world` (eventual) | – |
| `loc_greenhollow_nation` | Greenhollow             | nation   | `loc_sunspire_world` (eventual) | – |
| `loc_karak_thul_nation`  | Karak Thul              | nation   | `loc_sunspire_world` (eventual) | Sometimes written `Karak-Thul` |
| `loc_skraggmar_nation`   | Skraggmar               | nation   | `loc_sunspire_world` (eventual) | – |
| `loc_thra_zhul_nation`   | Thra Zhul               | nation   | `loc_sunspire_world` (eventual) | Sometimes written `Thrazhul` / `Thra-Zhul` |
| `loc_xorath_kul_nation`  | Xorath Kul              | nation   | `loc_sunspire_world` (eventual) | Sometimes written `Xorath-Kul` |
| `loc_big_titty_demon_island_region` | Big Titty Demon Island | region   | `loc_sunspire_world` (eventual) | Variants: `Big Tiddy Deamon Island` (Map), `Big Titty Island` |

> Rule of thumb: **JSON uses the short canonical name** (e.g. `Sylvara`) in `name`, and any extended title (e.g. “Sylvara: The Elven Forests”) goes in `summary` / Markdown.

### 2.3 Cities

| ID                    | Name        | Category | Parent ID             | Known variants / typos |
|-----------------------|-------------|----------|-----------------------|------------------------|
| `loc_eldenhold_city`  | Eldenhold   | city     | `loc_valeria_nation`  | – |
| `loc_ashenvale_city`  | Ashenvale   | city     | `loc_valeria_nation`  | – |
| `loc_port_town_city`  | Port Town   | city     | `loc_valeria_nation`  | “Pot Town” (typo) |
| `loc_gravenhollow_city` | Gravenhollow | city  | `loc_mireholm_nation` | – |

### 2.4 Sub-locations / Sites

BTDI and city-level maps will use `site` / `region` for local places.

| ID                                   | Name                  | Category | Parent ID                             | Known variants / typos                 |
|--------------------------------------|-----------------------|----------|----------------------------------------|----------------------------------------|
| `loc_big_titty_island_coast_region`  | Big Titty Island Coast | region  | `loc_big_titty_demon_island_region`   | Map `Map` field may use `Big Tiddy Deamon Island` |
| `loc_crystal_hinge_site`             | Crystal Hinge         | site     | `loc_big_titty_demon_island_region`   | – |
| `loc_eldenhold_<building>_site`      | \<Building Name\>     | site     | `loc_eldenhold_city`                  | Pattern only – per-building sites |
| `loc_port_town_<building>_site`      | \<Building Name\>     | site     | `loc_port_town_city`                  | Pattern only – per-building sites |
| `loc_gravenhollow_<building>_site`   | \<Building Name\>     | site     | `loc_gravenhollow_city`               | Pattern only – per-building sites |

Patterns like `loc_eldenhold_drunken_wyvern_site` are **allowed** and should follow:

- `loc_<city>_<slug>_site`
- `name` = “Drunken Wyvern” (or whatever)
- `category` = `"site"`
- `parent_location_id` = city ID

---

## 3. Usage Rules

1. **IDs never change.**  
   If a name changes, update only the `name` and text fields, not the `id`.

2. **Categories are fixed per row.**  
   - `world`, `nation`, `region`, `city`, `site` are the only categories used here.
   - BTDI is a **region**, not a nation.

3. **Parent IDs define the hierarchy.**  
   - Nations eventually point to `loc_sunspire_world`.
   - Cities always point to their nation.
   - Sites always point to a city or region.

4. **Known variants are for cleanup & import logic.**  
   - If any script or AI sees `Pot Town`, it should normalize to `Port Town`.
   - If it sees `Big Tiddy Deamon Island`, normalize to `Big Titty Demon Island`.

This file should be updated whenever:

- A new nation, city, or major site is added
- A naming decision changes (rename, recategorize, etc.)
