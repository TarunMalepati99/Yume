import os
import json
import yaml
import pickle
from typing import Any, List, Optional
from pathlib import Path

from PIL import Image


# ----------------------------
# Directory Helpers
# ----------------------------

def ensure_dir(path: str | Path) -> Path:
    """
    Create directory if it doesn't exist.
    Returns the Path object.
    """
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def list_files(
    directory: str | Path,
    extensions: Optional[List[str]] = None,
    recursive: bool = False,
) -> List[Path]:
    """
    List files in a directory optionally filtered by extension.
    """
    directory = Path(directory)

    if not directory.exists():
        return []

    if extensions:
        extensions = [ext.lower() for ext in extensions]

    files = []

    if recursive:
        for file in directory.rglob("*"):
            if file.is_file() and (extensions is None or file.suffix.lower() in extensions):
                files.append(file)
    else:
        for file in directory.iterdir():
            if file.is_file() and (extensions is None or file.suffix.lower() in extensions):
                files.append(file)

    return files


# ----------------------------
# Text I/O
# ----------------------------

def read_text(path: str | Path) -> str:
    """Read a UTF-8 text file."""
    return Path(path).read_text(encoding="utf-8")


def write_text(path: str | Path, text: str):
    """Write text to file, creating dirs if necessary."""
    path = Path(path)
    ensure_dir(path.parent)
    path.write_text(text, encoding="utf-8")


# ----------------------------
# JSON I/O
# ----------------------------

def read_json(path: str | Path) -> Any:
    """Load JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str | Path, data: Any, indent: int = 2):
    """Save JSON file with indenting."""
    path = Path(path)
    ensure_dir(path.parent)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


# ----------------------------
# YAML I/O
# ----------------------------

def read_yaml(path: str | Path) -> Any:
    """Load YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def write_yaml(path: str | Path, data: Any):
    """Write YAML file."""
    path = Path(path)
    ensure_dir(path.parent)
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f)


# ----------------------------
# Pickle I/O
# ----------------------------

def save_pickle(path: str | Path, obj: Any):
    """Save any Python object."""
    path = Path(path)
    ensure_dir(path.parent)
    with open(path, "wb") as f:
        pickle.dump(obj, f)


def load_pickle(path: str | Path) -> Any:
    """Load a pickled Python object."""
    with open(path, "rb") as f:
        return pickle.load(f)


# ----------------------------
# Image I/O
# ----------------------------

def load_image(path: str | Path) -> Image.Image:
    """Load an image with PIL and ensure RGB."""
    return Image.open(path).convert("RGB")


def save_image(path: str | Path, image: Image.Image):
    """Save PIL image, ensuring the folder exists."""
    path = Path(path)
    ensure_dir(path.parent)
    image.save(path)


# ----------------------------
# Path Helpers
# ----------------------------

def file_stem(path: str | Path) -> str:
    """Return filename without extension."""
    return Path(path).stem


def file_extension(path: str | Path) -> str:
    """Return file extension including the dot."""
    return Path(path).suffix.lower()


def join_path(*parts) -> Path:
    """Join multiple path segments."""
    return Path(os.path.join(*map(str, parts)))

