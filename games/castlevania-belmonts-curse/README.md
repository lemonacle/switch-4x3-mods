# Castlevania: Belmont's Curse

## Full game 1.1.0

Download **Castlevania Belmonts Curse v1.1.0 Mods.zip** from [Releases](https://github.com/lemonacle/switch-4x3-mods/releases/latest).
It contains selectable 4:3, RenderScale Fix, and R3 Manual Zoom components.
All are asset-free; no builder is required. See the [master README](full-1.1.0/README.md) for installation, compatibility, and limitations.

## Demo 1.0.0

The unchanged demo V7.1 patch remains in the [original release](https://github.com/lemonacle/switch-4x3-mods/releases/tag/belmonts-curse-v1).
Title ID: `0100D1D027E96000`; build ID: `07C3F500203A719B9F06025D0982DCF7`.
Import the demo ZIP as a mod, enable it, set Eden to 4:3, and restart.
Extra vertical view can reveal unfinished scenery. Do not use full-game patches with the demo.

The legacy demo-only RenderScale asset builder remains available for users with their own matching RomFS:

```text
python -m pip install -r tools/requirements.txt
python tools/build_render_scale.py demo-1.0.0 --romfs "PATH/TO/DEMO/ROMFS"
```

Its generated ZIP contains locally modified game data; keep it private. It changes the initial preset only and does not include the full game's runtime scale fix. The demo has not been ported to the new asset-free RenderScale implementation.
