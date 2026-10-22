# Castlevania: Belmont's Curse v1.1.0 Mods

Three optional components from the same 4:3 project. Pick the features you need.
All included mods are executable patches: no game assets, RomFS dump, or builder required.

**Compatibility:** full Switch game **1.1.0**, title ID `0100BA4026E94000`,
executable build ID `0F1169AA7D0FA4529C861F96ADEC306E`.
These are Eden-compatible `.pchtxt` patches. Native Switch hardware is not validated.

## Choose your mods

| Folder | Purpose | Requirements |
| --- | --- | --- |
| `4x3 v7.2 (1.1.0)` | 1280x960 framing, menu fixes, camera tracking corrections, title/loading and video letterboxing | Set emulator aspect ratio to 4:3 |
| `RenderScale Fix v3 (1.1.0)` | Keeps internal rendering at 1.0 at startup and through runtime scale changes | Independent of 4:3; increases GPU workload compared with reduced rendering |
| `Manual-Zoom v3 (1.1.0)` | R3 toggles expanded framing and a closer, original-height view on tracking cameras | Requires the included 4:3 mod; omit if R3 is needed by another mod |

RenderScale and 4:3 work independently or together. Manual Zoom is optional;
the 4:3 mod does not require it. No automatic boundary-driven zoom is included.

## Installation

1. Extract this release ZIP on your computer. It is a collection, not a single mod to import wholesale.
2. Disable older versions of the selected mods, including separate video fixes and old RenderScale asset/runtime packages.
3. Open the game's mod directory in your emulator. Copy only the named mod folders you want into it. Each folder must directly contain `exefs`.
4. Enable your selected mods. Use 4:3 in emulator settings when enabling the 4:3 mod.
5. Fully restart the game.

For example, the game mod directory can contain:

```text
0100BA4026E94000/
  4x3 v7.2 (1.1.0)/exefs/...
  RenderScale Fix v3 (1.1.0)/exefs/...
  Manual-Zoom v3 (1.1.0)/exefs/...
```

If using an emulator folder importer, import each chosen named folder separately.
Keep this README, camera reports, checksums, and license on your computer; they
are not needed by the game and should not be copied into individual mod folders.
Do not enable multiple versions of the same component. Other mods that alter the
same instructions may conflict even if they use different names. Disable a mod
and restart to revert it; these patches do not modify saves.

## Behavior and limitations

The 4:3 view preserves horizontal coverage and adds vertical view. This can expose
unfinished scenery. Menus fit the screen, while title/loading imagery and videos
retain appropriate letterboxing. The video fix uses the shared playback controller;
the opening has been confirmed, but every later cutscene has not been validated.

RenderScale applies both at camera preparation and when the game's scale manager
requests changes. The user confirmed the asset-free version, including the earlier
save-menu -> gameplay -> main-menu -> save-menu sharpness regression. This replaces
the old asset-based approach for the full game. It does not set the emulator's own
resolution multiplier.

Manual Zoom leaves static/fixed and rail cameras at normal expanded framing. Your
zoom choice is remembered across those exclusions and resumes on tracking cameras.
R3 presses during exclusions are ignored; holding R3 across an exit does not count
as another click. Restart resets the choice. Existing game R3 actions remain active,
so avoid combining this component with another R3-driven mod unless intended.
Script-controlled cameras may need further testing.

The combined packages were reported working by the user. Patch bytes were preserved
from those packages and checked for overlap between these three components. This is
not a claim that every room, camera transition, or device has been tested.

## Supporting reports and adaptation

`camera-audit.md` and `camera-inventory.csv` describe camera classifications used
for Manual Zoom. **Internal scene names may contain spoilers.** These are inspection
reports, not extracted game assets. Counts describe serialized camera candidates,
not confirmed gameplay failures. `SHA256SUMS.txt` checks the package files.

The separate folders make it possible to use just RenderScale, omit R3 zoom, or
study one implementation when adapting a mod to another display setup. Patches
are build-specific; renaming a file does not port it to another update or ratio.

Project and additional resources: https://github.com/lemonacle/switch-4x3-mods
Original contributions are MIT licensed; see `LICENSE`. No game data is distributed.
