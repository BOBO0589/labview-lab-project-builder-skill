from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def resolve_url(project_path: Path, url: str) -> Path:
    if url.startswith("file:///"):
        return Path(url[8:])
    if len(url) > 2 and url[1] == ":":
        return Path(url)
    rel = url.replace("/", "\\")
    if rel.startswith("..\\"):
        rel = rel[3:]
    return project_path.parent / rel


def validate(project_path: Path) -> list[tuple[str, str, Path]]:
    tree = ET.parse(project_path)
    missing: list[tuple[str, str, Path]] = []
    for item in tree.findall(".//Item"):
        url = item.attrib.get("URL")
        if not url:
            continue
        target = resolve_url(project_path, url)
        if not target.exists():
            missing.append((item.attrib.get("Name", ""), url, target))
    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate that LabVIEW .lvproj Item URL targets exist.")
    parser.add_argument("project", type=Path)
    args = parser.parse_args()

    project = args.project.resolve()
    if not project.exists():
        print(f"ERROR: project not found: {project}", file=sys.stderr)
        return 2

    try:
        missing = validate(project)
    except ET.ParseError as exc:
        print(f"ERROR: invalid XML: {exc}", file=sys.stderr)
        return 3

    if missing:
        print(f"MISSING {len(missing)} references in {project}")
        for name, url, target in missing:
            print(f"- {name}: {url} -> {target}")
        return 1

    print(f"ALL_PATHS_OK {project}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
