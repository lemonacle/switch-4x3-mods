# Castlevania: Belmont's Curse

| Edition | Version | Title ID | Executable build ID |
| --- | --- | --- | --- |
| Demo | 1.0.0 | `0100D1D027E96000` | `07C3F500203A719B9F06025D0982DCF7` |
| Full game | 1.1.0 | `0100BA4026E94000` | `0F1169AA7D0FA4529C861F96ADEC306E` |

## 4:3 patch

The demo package is V7.1. The full-game package is its build-specific v2 port.

- Requests 1280x960.
- Preserves gameplay's horizontal coverage and shows additional vertical view.
- Fits menus to width and corrects the scale change during the world-space menu transition.
- Letterboxes title/loading cameras within the 4:3 screen.
- Uses the original-height camera-confinement footprint to address tracking through short sections.

**Known limitation:** the extra vertical view can reveal unfinished scenery. Adaptive zoom is not included. New rooms, scripted cameras, and cutscenes still need testing. Full-game testing so far is positive initial Nova feedback, not a completed full-game validation. Render Scale 1x has not been independently confirmed by that feedback.

### Install in Eden

1. Download the ZIP for your edition from [Releases](https://github.com/lemonacle/switch-4x3-mods/releases/latest).
2. Import it as a mod for that game and enable it.
3. Set the emulator's aspect ratio to **4:3**.
4. Disable other aspect/resolution patches and fully restart the game.

For manual installation, put the included `exefs` folder inside a named mod folder under the game's emulator mod directory. Do not rename a demo patch to use it with the full game.

Full-game users upgrading from the first unsuccessful ports should disable `4x3-v7.1-Full-v1` and `RenderScale-1x-Full-v1`. Use the 1.1.0 v2 packages instead.

To roll back, disable the mod and restart. These patches do not edit saves.

## Optional Render Scale 1x

This raises the Low graphics preset's render scale from **70% to 100%** for both supported editions. It increases GPU workload and does not itself change aspect ratio. Test the 4:3 patch alone first.

No replacement game bundle is distributed. Build the mod locally from your own matching RomFS:

```text
python -m pip install -r tools/requirements.txt
python tools/build_render_scale.py demo-1.0.0 --romfs "PATH/TO/DEMO/ROMFS"
python tools/build_render_scale.py full-1.1.0 --romfs "PATH/TO/FULL/ROMFS-1.1.0"
```

Run only the command for your edition. The RomFS folder must contain `Data/`. The builder checks the original bundle's SHA-256, edits only `RedWine_URP_Settings_Low.m_RenderScale`, reopens and verifies the result, and creates an import ZIP in `local-output/`. Install that ZIP separately; it can be enabled alongside the matching 4:3 patch. Keep the generated ZIP local.

The input hash is identical for these two settings bundles, but their filenames differ. The builder uses the appropriate filename for each edition.

## Preservation and validation

The repository retains the patch definitions, build IDs, a hash-checked asset builder, and instructions. Recreating the optional asset mod requires an original matching bundle; existing locally generated mods remain usable without retaining the entire dump. No game backup is archived here.

Executable patch sites and helper branches were checked against the supported binaries. Asset-builder tests verified that only the intended settings property changed. Release ZIPs contain only patch text. The abandoned experimental zoom variants and the superseded earlier full-game build are not included.
