---
name: labview-lab-project-builder
description: Build or repair LabVIEW coursework packages for labs, experiments, and course designs. Use when Codex needs to create a deliverable LabVIEW folder containing .lvproj files, real .vi/.ctl/.lvlib references copied from installed LabVIEW examples, reports, generated results, launch scripts, validation checks, and zip archives; also use when fixing broken LabVIEW project paths, Chinese/English project labels, or packaging previous LabVIEW work into reusable submissions.
---

# LabVIEW Lab Project Builder

## Core Workflow

1. Inspect the user requirements from screenshots or text and separate formal deliverables from examples that should not be implemented.
2. Locate LabVIEW with `LABVIEW_HOME`, common install paths such as `C:\Multisim12\LabVIEW 2025`, or the running `LabVIEW.exe` process.
3. Search installed examples first with `rg --files "<LabVIEW>\examples"` and copy real `.vi`, `.ctl`, `.lvlib`, and support folders that match the assignment.
4. Build a clean project directory under the user's requested workspace, usually `C:\LABVI\<project-name>`.
5. Create an `.lvproj` that references copied real VI files and keeps supporting docs/results in project folders.
6. Generate report files, result data, screenshots, and launch scripts.
7. Validate every `Item URL` in the `.lvproj`, run deterministic simulation scripts, open the project with LabVIEW when possible, and zip the final folder.

Never claim that a generated placeholder is a custom binary VI. If true VI synthesis is not reliable, use real copied LabVIEW examples as the executable VI base and document the required front-panel/block-diagram edits.

## Choosing Real VI Bases

Prefer installed LabVIEW examples over web downloads. Read `references/example-map.md` when selecting examples for common coursework topics.

Use these patterns:

- Signal generation, filtering, FFT: copy Signal Processing examples and their `subVIs`.
- Arrays and strings: copy examples from `examples\Arrays` and `examples\Strings`.
- Real-time monitoring/control: copy `examples\Industry Applications\Temperature Monitoring`.
- UI events, gestures, audio, Python bridge: copy examples under `Structures\Event Structure`, `Graphics and Sound\Sound`, `Channels\Messenger`, and `Connectivity\Python`.

When copying an example tree, use PowerShell `Copy-Item -Path (Join-Path $src '*') -Destination $dst -Recurse -Force`; copying the literal directory path into an existing destination can accidentally nest or omit expected contents.

## Project File Rules

Use ASCII filenames for copied VI files when LabVIEW path handling is fragile, but use Chinese `Item Name` labels in the project tree when the course is Chinese.

Relative URLs should be relative to the `.lvproj` file location. For project-root files, use `../file` only when matching the LabVIEW example style; validate paths after generation. If a generated project fails to open, first check for mojibake in XML, invalid XML escaping, and missing target files.

Use `scripts/create_lvproj_from_manifest.py` for repeatable project generation. Use `scripts/validate_lvproj_paths.py` before final delivery.

## Deliverable Checklist

For each lab/coursework package, include:

- `.lvproj` and `.aliases`
- Real `.vi` files and any dependency folders they need
- `README_*.md` or usage notes only when the user needs them outside the skill output
- Report `.md`, `.docx`, and optional `.html`
- Result data such as `.csv`/`.json`
- Result images/screenshots where helpful
- `打开...工程.bat` launch script
- `重新生成...结果.bat` for deterministic simulation outputs
- Final `.zip` in the parent submission directory

## Validation

Run:

```powershell
python <skill>\scripts\validate_lvproj_paths.py C:\LABVI\LabVIEW_lab3\lab3.lvproj
```

Also run any simulation scripts, inspect generated CSV/JSON, and open generated PNGs with a simple image check when screenshots are part of the submission.

For LabVIEW launch validation:

```powershell
Start-Process -FilePath "<LabVIEW>\LabVIEW.exe" -ArgumentList "C:\LABVI\...\project.lvproj" -WindowStyle Hidden
```

Stop the process afterward if the user does not need it left open.
