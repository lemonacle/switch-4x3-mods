# Full-game 1.1.0 camera audit

Examined the user-provided extracted RomFS and executable, read only. Build: `0F1169AA7D0FA4529C861F96ADEC306E`.

## Scope and findings

- 442 catalogued scenes read successfully; 384 are under World_Biome paths. Other scenes include gyms, prototypes, menus and setup scenes.
- All 34 biome scenes with SaveRoom in their names contain a static camera.
- 109 biome scenes contain static camera candidates (123 camera instances). 75 of these scenes have neither a SaveRoom name nor a SavePoint component.
- 50 biome scenes contain rail camera candidates (77 camera instances).
- One additional biome scene has a SavePoint component without a SaveRoom name; its scene-local camera candidates are tracking cameras. The presence of a save object alone is not sufficient reason to exclude an entire room.

These are serialized camera candidates, including disabled cameras activated by triggers, cinematic cameras and alternate states. A static camera existing in a scene does not mean ordinary gameplay in the whole scene is fixed. The runtime patch uses the active camera classification instead of disabling zoom for every scene in this inventory.

## Evidence and method

The Addressables catalogue supplied each scene bundle. The shared MonoScript bundle resolved script identifiers. Each primary scene bundle was inspected for GameObjects, Transforms, CinemachineVirtualCamera, Cinemachine body components, gameplay camera controls, and save-point components. Camera component-owner transforms associate the body pipeline with each virtual camera. Transposer bodies are recorded as tracking candidates, TrackedDolly bodies as rail candidates, and cameras without either as static candidates.

In the inspected StreetsPoor_SaveRoom02_uid78 scene, the room-entry event enables GPE_PunctualVirtualCamera and the room-leave event disables it. That virtual camera has no tracking or dolly body. The same scene also contains a separate first-save sequence camera with a Transposer body. This is why an active-camera rule is preferable to a whole-scene blacklist.

Executable inspection of CameraManagerSystem.GetVirtualCameraType shows the existing classifier returning 1 for the first supported body, 2 for the second, and 0 for neither; the metadata names these types Transposer, Rail and Static. UpdateCameraDistanceFromScreenHeight retains this resolved value in w22 at the existing manual-zoom hook. The game itself has a HOTFIX_DisableCameraZoomOnStaticAndRail setting, providing further evidence that these camera types warrant special zoom handling.

## Test 3 policy

- Tracking camera (Transposer / 1): keep Test 2 behavior; R3 selects expanded or V4 authored-height framing.
- Static (0), rail (2), or unknown type: return the stable mod's normal expanded height and leave the remembered zoom bit unchanged.
- Update the held-button bit during exclusions but ignore toggle presses there. This prevents a held button from becoming a new click when exiting.
- Do not change native camera tracking, room assets, saves, scripted camera effects or the stable aspect-ratio patch.

## Validation and limits

Native compiled tests passed for 100 transition cycles, tracking/static/rail/unknown types, held input, ignored presses during exclusions, remembered zoom on exit, normal framing on entry/exit, and initialization-bit preservation. Static checks verify the original call site, w22 dataflow, code space, incoming direct branches, instruction decoding and lack of overlap with stable 4:3 v2. In-game testing of Test 3 remains pending.

Scripts can temporarily hold a tracking camera still or replace its follow target without changing its body type. Those cases are not guaranteed to be identified by this rule. This audit also does not simulate camera activation, blends, gameplay state or every conditionally instantiated prefab. Camera candidates in the CSV are not a claim of observed bad framing.

## Biome inventory

| Internal biome | Scenes | SaveRoom names | Scenes with static candidates | Scenes with rail candidates |
|---|---:|---:|---:|---:|
| World_Biome_01_Streets_Poor | 50 | 5 | 16 | 2 |
| World_Biome_02_InnocentsCemetery | 43 | 4 | 18 | 4 |
| World_Biome_03_Catacombs | 43 | 2 | 7 | 0 |
| World_Biome_05_NotreDame | 42 | 3 | 19 | 8 |
| World_Biome_06_MainHall | 59 | 9 | 14 | 11 |
| World_Biome_08_Library | 38 | 2 | 12 | 1 |
| World_Biome_09_ClockTower | 53 | 3 | 8 | 9 |
| World_Biome_10_HallOfMirrors | 42 | 5 | 9 | 15 |
| World_Biome_11_MasterQuarter | 9 | 1 | 2 | 0 |
| World_Biome_12_MQBadEnding | 5 | 0 | 4 | 0 |

The accompanying camera-inventory.csv lists every scene-local virtual camera found across all 442 scenes. Internal camera and scene names may reveal locations or events.
