"""Build a local Render Scale 1x mod from an original, supported RomFS bundle."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import zipfile


def build(edition, romfs, output):
    import UnityPy

    root = Path(__file__).resolve().parents[1]
    config = json.loads((root / "games/castlevania-belmonts-curse/builds.json").read_text())
    spec = config[edition]
    relative = Path("Data/StreamingAssets/aa/Switch") / spec["render_scale_bundle"]
    source = romfs / relative
    raw = source.read_bytes()
    if hashlib.sha256(raw).hexdigest() != spec["original_bundle_sha256"]:
        raise ValueError("Original bundle hash does not match this supported build. Nothing written.")
    env = UnityPy.load(raw)
    before = {(o.assets_file.name, o.path_id): o.get_raw_data() for o in env.objects}
    matches = [o for o in env.objects if o.path_id == spec["render_scale_path_id"]]
    if len(matches) != 1:
        raise ValueError("Expected exactly one settings object.")
    obj = matches[0]
    tree = obj.read_typetree()
    if tree.get("m_Name") != "RedWine_URP_Settings_Low":
        raise ValueError("Settings object name does not match.")
    if not math.isclose(tree["m_RenderScale"], 0.7, abs_tol=1e-6):
        raise ValueError("Expected the original 70% render scale.")
    tree["m_RenderScale"] = 1.0
    obj.save_typetree(tree)
    payload = env.file.save()
    reopened = UnityPy.load(payload)
    after = {(o.assets_file.name, o.path_id): o.get_raw_data() for o in reopened.objects}
    target = (obj.assets_file.name, obj.path_id)
    if before.keys() != after.keys() or [k for k in before if before[k] != after[k]] != [target]:
        raise ValueError("Unexpected bundle changes; nothing written.")
    actual = next(o for o in reopened.objects if o.path_id == obj.path_id).read_typetree()
    if actual != tree:
        raise ValueError("Saved settings do not match; nothing written.")
    output.mkdir(parents=True, exist_ok=True)
    zip_path = output / f"Belmonts-Curse-{edition}-RenderScale-1x.zip"
    # Exclusive creation avoids overwriting an existing local mod.
    with zipfile.ZipFile(zip_path, "x", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("romfs/" + relative.as_posix(), payload)
    with zipfile.ZipFile(zip_path) as archive:
        if archive.testzip() is not None:
            raise ValueError("ZIP integrity check failed.")
    print(f"Created {zip_path.resolve()}")
    print("This generated ZIP contains your locally modified game bundle. Do not commit it.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("edition", choices=["demo-1.0.0", "full-1.1.0"])
    parser.add_argument("--romfs", required=True, type=Path, help="Extracted RomFS folder containing Data/")
    parser.add_argument("--output", type=Path, default=Path("local-output"))
    args = parser.parse_args()
    try:
        build(args.edition, args.romfs, args.output)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Error: {exc}\n")
