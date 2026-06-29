from pathlib import Path
from urllib.parse import quote


BASE_URL = "https://jing67023-eng.github.io/koko-stickers/stickers"
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif"}
PROJECT_DIR = Path(__file__).resolve().parent
STICKERS_DIR = PROJECT_DIR / "stickers"
OUTPUT_FILE = PROJECT_DIR / "koko_import.txt"


def main() -> int:
    if not STICKERS_DIR.is_dir():
        print(f"Missing stickers directory: {STICKERS_DIR}")
        return 1

    sticker_files = sorted(
        path
        for path in STICKERS_DIR.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )

    if not sticker_files:
        print("No supported sticker files found.")
        return 1

    lines = []
    skipped = []
    for path in sticker_files:
        if " " in path.name:
            skipped.append(path.name)
            continue

        sticker_name = path.stem
        url_name = quote(path.name)
        lines.append(f"{sticker_name} {BASE_URL}/{url_name}")

    OUTPUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Generated {OUTPUT_FILE.name}: {len(lines)} stickers")
    if skipped:
        print("Skipped files with spaces:")
        for name in skipped:
            print(f"- {name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
