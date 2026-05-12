from __future__ import annotations

import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.dom import minidom


SERVER_PROPERTIES = [
    ("server.app.propertiesEnabled", "Bool", "true"),
    ("server.control.propertiesEnabled", "Bool", "true"),
    ("server.tcp.enabled", "Bool", "false"),
    ("server.tcp.port", "Int", "0"),
    ("server.tcp.serviceName", "Str", "My Computer/VI Server"),
    ("server.tcp.serviceName.default", "Str", "My Computer/VI Server"),
    ("server.vi.callsEnabled", "Bool", "true"),
    ("server.vi.propertiesEnabled", "Bool", "true"),
    ("specify.custom.address", "Bool", "false"),
]


def add_property(parent: ET.Element, name: str, typ: str, value: str) -> None:
    prop = ET.SubElement(parent, "Property", {"Name": name, "Type": typ})
    prop.text = value


def add_folder(parent: ET.Element, folder: dict) -> None:
    folder_el = ET.SubElement(parent, "Item", {"Name": folder["name"], "Type": "Folder"})
    for item in folder.get("items", []):
        ET.SubElement(
            folder_el,
            "Item",
            {
                "Name": item["name"],
                "Type": item.get("type", "VI"),
                "URL": item["url"],
            },
        )


def build_project(manifest: dict) -> ET.ElementTree:
    project = ET.Element("Project", {"Type": "Project", "LVVersion": manifest.get("lv_version", "25008000")})
    add_property(project, "NI.LV.All.SaveVersion", "Str", "Editor version")
    add_property(project, "NI.LV.All.SourceOnly", "Bool", str(manifest.get("source_only", False)).lower())
    if manifest.get("description"):
        add_property(project, "NI.Project.Description", "Str", manifest["description"])

    computer = ET.SubElement(project, "Item", {"Name": "My Computer", "Type": "My Computer"})
    for name, typ, value in SERVER_PROPERTIES:
        add_property(computer, name, typ, value)

    for folder in manifest.get("folders", []):
        add_folder(computer, folder)

    ET.SubElement(computer, "Item", {"Name": "Dependencies", "Type": "Dependencies"})
    ET.SubElement(computer, "Item", {"Name": "Build Specifications", "Type": "Build"})
    return ET.ElementTree(project)


def write_pretty(tree: ET.ElementTree, path: Path) -> None:
    raw = ET.tostring(tree.getroot(), encoding="utf-8")
    pretty = minidom.parseString(raw).toprettyxml(indent="\t", encoding="UTF-8").decode("utf-8")
    pretty = pretty.replace('<?xml version="1.0" encoding="UTF-8"?>', "<?xml version='1.0' encoding='UTF-8'?>")
    path.write_text(pretty, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a LabVIEW .lvproj from a JSON manifest.")
    parser.add_argument("manifest", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    tree = build_project(manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    write_pretty(tree, args.output)
    print(f"WROTE {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
