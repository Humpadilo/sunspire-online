"""
dump_repo_tree.py

Creates a filtered inventory of folders/files under SunspireOnlinePublic.
- Skips junk (.venv, node_modules, __pycache__, .git, etc.)
- Outputs:
  1) a pretty tree view
  2) a flat CSV-ish list with paths

Run:
  python tools/dump_repo_tree.py

Outputs to:
  docs/file_inventory/repo_tree.txt
  docs/file_inventory/repo_files.txt
"""

from pathlib import Path

ROOT = Path(r"D:\SunspireOnlinePublic")

# Folders to skip entirely
SKIP_DIRS = {
    ".git", ".github", ".venv", "venv", "env",
    "__pycache__", ".pytest_cache", ".mypy_cache",
    "node_modules", ".next", "dist", "build", "out",
    ".vscode", ".idea", ".cache",
}

# File extensions to skip (you can add more)
SKIP_EXTS = {
    ".pyc", ".pyo", ".log", ".tmp",
}

def should_skip_dir(p: Path) -> bool:
    return p.name in SKIP_DIRS

def should_skip_file(p: Path) -> bool:
    return p.suffix.lower() in SKIP_EXTS

def build_tree(root: Path):
    lines = []
    def walk(dir_path: Path, prefix=""):
        entries = sorted(
            [e for e in dir_path.iterdir() if not should_skip_dir(e)],
            key=lambda x: (x.is_file(), x.name.lower())
        )
        for i, e in enumerate(entries):
            connector = "└── " if i == len(entries) - 1 else "├── "
            lines.append(f"{prefix}{connector}{e.name}")
            if e.is_dir():
                extension = "    " if i == len(entries) - 1 else "│   "
                walk(e, prefix + extension)
    lines.append(root.name)
    walk(root)
    return "\n".join(lines)

def build_file_list(root: Path):
    files = []
    for p in root.rglob("*"):
        if p.is_dir():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if should_skip_file(p):
            continue
        rel = p.relative_to(root)
        files.append(str(rel).replace("\\", "/"))
    return "\n".join(sorted(files))

def main():
    out_dir = ROOT / "docs" / "file_inventory"
    out_dir.mkdir(parents=True, exist_ok=True)

    tree_txt = build_tree(ROOT)
    files_txt = build_file_list(ROOT)

    (out_dir / "repo_tree.txt").write_text(tree_txt, encoding="utf-8")
    (out_dir / "repo_files.txt").write_text(files_txt, encoding="utf-8")

    print("Wrote:")
    print(out_dir / "repo_tree.txt")
    print(out_dir / "repo_files.txt")

if __name__ == "__main__":
    main()
