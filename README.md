# Switch 4:3 Mods

Nintendo Switch 4:3 patches and practical notes, with testing focused on the Retroid Pocket Nova and Eden. **Patches and tools only: no games, extracted assets, firmware, keys, or saves.**

## Downloads

Get the patch-only ZIPs from **[Releases](https://github.com/lemonacle/switch-4x3-mods/releases/latest)**.

| Game | Supported version | Included work | Testing |
| --- | --- | --- | --- |
| [Castlevania: Belmont's Curse Demo](games/castlevania-belmonts-curse/README.md) | 1.0.0 | 4:3 V7.1; optional local Render Scale 1x builder | Demo 4:3 tested during play on Nova and PC emulator |
| [Castlevania: Belmont's Curse](games/castlevania-belmonts-curse/README.md) | 1.1.0 | 4:3 v4, asset-free RenderScale Fix v3, optional R3 Manual Zoom v3 in one ZIP | User-confirmed packages; not every room/cutscene validated |

Match the **title ID and executable build ID**, not just the game name. A patch for the demo or another update will not necessarily work. These packages target emulator `.pchtxt` support; native Switch hardware has not been tested.

## Find an existing mod first

This is a small collection, not a complete Switch mod index. Before requesting or developing a new fix, check these projects:

| Project | What to look for |
| --- | --- |
| [pakrett / Aspect-Ratio-Mods](https://github.com/pakrett/Aspect-Ratio-Mods) | A collection focused on 4:3 displays; start with its Switch section. |
| [StevensND / switch-port-mods](https://github.com/StevensND/switch-port-mods) | Per-game Switch emulator mods, including aspect-ratio and performance work. Read each game's supported versions. |
| [pacoa-kdbg / Switch-Emulator-Ultrawide-FPS-Mods](https://github.com/pacoa-kdbg/Switch-Emulator-Ultrawide-FPS-Mods) | Another place to search for game-specific aspect-ratio and FPS work. Check the actual ratios offered. |
| [yuzu-mirror / yuzu-mod-archive](https://github.com/yuzu-mirror/yuzu-mod-archive) | Historical mod listings with version and author information. This is a mirror, not the original emulator organization. |

These links are discovery resources, **not compatibility endorsements**. Not every mod in them supports 4:3, Eden, or your game update. Prefer the original author's release and instructions, and link upstream rather than copying their work here.

## Want to make or update a mod?

Start with the **[contributor guide and resources](docs/CONTRIBUTING.md)**. It covers finding prior work, matching builds, distinguishing stretching from cropping, UI and camera pitfalls, and publishing patches without game data.

Useful starting points:

- [StevensND's Ghidra/IDA and aspect-ratio porting guide](https://github.com/StevensND/ghidra-port-mods-guide)
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra)
- [UnityPy](https://github.com/K0lb3/UnityPy), for inspecting Unity assets from your own dumps
- [Capstone](https://github.com/capstone-engine/capstone), for instruction inspection

I've also worked on 4:3 fixes for PC games—you can find those on [my GitHub profile](https://github.com/lemonacle).

## Reporting an issue

Include the title ID, game version/build ID, emulator version, device, enabled mods, aspect-ratio setting, and the room or menu where it happens. A comparison from the same position with the mod disabled is especially useful. Redact personal paths from logs. Do not upload dumps, keys, saves, or extracted game bundles.

Original scripts, documentation, and patch contributions here are MIT licensed. Linked projects retain their own authorship and licenses. Game names identify compatibility; this repository is not affiliated with the developers or publishers.
