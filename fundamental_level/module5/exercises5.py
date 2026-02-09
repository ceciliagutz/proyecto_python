# Modulo Libreria estandar E/S

import csv
import json
import logging
import subprocess
from datetime import datetime
from pathlib import Path


# PathLib
def create_text_file(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# Json


def save_json(path: Path, data: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


# CSV
def read_csv(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


# Datetime


def get_current_timestamp() -> str:
    return datetime.now().isoformat()


# Logging


def setup_logger() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


# Subprocess


def run_echo_command(message: str) -> str:
    result = subprocess.run(
        ["cmd", "/c", "echo", message],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


# Test
if __name__ == "__main__":
    base = Path("test_data")
    base.mkdir(exist_ok=True)

    text_file = base / "example.txt"
    json_file = base / "date.json"

    create_text_file(text_file, "Hi Cecilia Gutierrez")
    print(read_text_file(text_file))

    save_json(json_file, {"name": "Cecilia", "age": 24})
    print(load_json(json_file))

    print(get_current_timestamp())

    setup_logger()
    logging.info("This is an info log")

    print(run_echo_command("Hello from subprocess"))
