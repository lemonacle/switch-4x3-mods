# Finding, developing, and sharing a Switch 4:3 mod

## Check existing work

Search the collections linked in the [main README](../README.md), using both the game's name and title ID. Search the original repository's issues and releases for your update and desired aspect ratio. If a working mod already exists, a link and a useful compatibility note are preferable to a duplicate.

When adapting existing work, identify the author, link the exact source, and follow its license. A public repository is not automatically permission to redistribute its contents. The external projects listed here are references; the Castlevania packages do not contain their mods.

## Identify the exact build

Record the title ID, displayed game version, and executable build ID. Select the intended update before extracting ExeFS/RomFS. Hash the original files used as inputs. Keep base-game and updated dumps separate locally.

The Castlevania full-game first port targeted an earlier dump and did not work on 1.1.0. The corrected port relocated the executable patches and used 1.1.0's asset bundle name. Simply changing the build-ID header would not have fixed the addresses.

## Decide what 4:3 should mean

- **Stretching:** the same scene is distorted to fill a different shape.
- **Cropping:** correct proportions, but part of the original scene is removed.
- **Expanded view:** preserves the original horizontal coverage and reveals more above/below.
- **Letterboxing:** fits fixed 16:9 artwork inside 4:3 with black bars above/below.

Different screens can need different choices. These Castlevania patches expand gameplay vertically, fit menus, and letterbox title/loading artwork.

## Inspect before patching

Use [StevensND's porting guide](https://github.com/StevensND/ghidra-port-mods-guide) for practical Ghidra/IDA and aspect-ratio starting points. [Ghidra](https://github.com/NationalSecurityAgency/ghidra) and [Capstone](https://github.com/capstone-engine/capstone) help inspect executable instructions; [UnityPy](https://github.com/K0lb3/UnityPy) can inspect supported Unity asset formats.

Find the resolution selection, camera aspect/FOV or orthographic size, UI scaling, and any special camera paths. Treat constants as candidates, not proof. Verify callers, inputs, original instructions, and branch targets before changing them. Revalidate every executable update.

For Unity projects, useful official explanations include:

- [Camera aspect](https://docs.unity3d.com/ScriptReference/Camera-aspect.html)
- [Camera viewport rectangle](https://docs.unity3d.com/ScriptReference/Camera-rect.html)
- [Orthographic camera size](https://docs.unity3d.com/ScriptReference/Camera-orthographicSize.html)
- [Canvas Scaler](https://docs.unity3d.com/Packages/com.unity.ugui@1.0/manual/script-CanvasScaler.html)

An engine setting is not necessarily the final value: animations, transitions, and late camera updates may overwrite it.

## Test the whole camera behavior

Test cold launch, title, loading, map, equipment, settings, cutscenes, short rooms, tall rooms, both directions through transitions, and return to title. Compare the same location and character position at stock 16:9.

Extra vertical view can expose unfinished scenery. Camera confinement may also assume the original frame shape: a taller footprint can stop a camera following the player into short sections. A fix that preserves tracking may still show scenery outside the intended view.

The demo's experimental automatic zoom attempts are deliberately not published as working fixes. They introduced tracking problems or failed to hide the intended scenery. Do not apply a global zoom adjustment solely because one room looks wrong.

## Publish changes, not game files

Share small executable patch definitions or a local patch builder with input-hash checks. Do not commit NSP/XCI/NCA files, original executables, asset bundles (including modified bundles), metadata dumps, firmware, keys, or saves.

For asset edits, verify that only the intended object/property changed after saving. Keep generated bundles local. Include install and rollback instructions, exact supported builds, known limitations, and an honest distinction between static validation and gameplay testing.

External links were checked on 2026-10-20. Projects may move; report broken links or a better upstream resource through an issue or pull request.
