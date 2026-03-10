# datasets/

Keep dataset metadata and scripts here.
Do not commit raw images/videos by default.

Suggested structure:
- `datasets/metadata/`  (CSV/JSON labels, class list, dataset cards)
- `datasets/samples/`   (a few small sample images)
- `datasets/raw/`       (ignored by git)
- `datasets/exports/`   (ignored by git)

For V1, document:
- classes to detect
- capture conditions (light level, distance)
- split strategy (train/val/test)
