import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
ATLAS_DIR = ROOT / "atlas"


def load_json(path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_directory(directory, schema_name):
    schema_path = SCHEMA_DIR / schema_name
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)

    files = sorted(directory.rglob("*.json"))
    errors = []

    for path in files:
        try:
            data = load_json(path)
        except Exception as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue

        for error in validator.iter_errors(data):
            location = ".".join(str(part) for part in error.absolute_path)
            suffix = f" at {location}" if location else ""
            errors.append(f"{path}: {error.message}{suffix}")

    return errors


def main():
    checks = [
        ("technologies", "technology.schema.json"),
        ("threats", "threat.schema.json"),
        ("attacks", "attack.schema.json"),
        ("defenses", "defense.schema.json"),
        ("detections", "detection.schema.json"),
        ("benchmarks", "benchmark.schema.json"),
        ("research", "research.schema.json"),
    ]

    all_errors = []

    for directory_name, schema_name in checks:
        directory = ATLAS_DIR / directory_name

        if not directory.exists():
            continue

        all_errors.extend(validate_directory(directory, schema_name))

    if all_errors:
        print("Atlas validation failed:\n")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print("Atlas validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())