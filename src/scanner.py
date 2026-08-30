from pathlib import Path
import hashlib
from datetime import datetime

def detect_file_type(file_path):
    with open(file_path, "rb") as file:
        header = file.read(8)
    if header.startswith(b"\x4D\x5A"):
        return "PE executable"
    if header.startswith(b"%PDF"):
        return "PDF document"
    if header.startswith(b"\x89PNG"):
        return "PNG image"
    if header.startswith(b"\xFF\xD8\xFF"):
        return "JPEG image"
    return "Unknown"


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

def scan_file(file_path):
    """
    Collect basic metadata about a file.
    """
    file = Path(file_path)
    if not file.exists():
        return None
    file_info = {
        "name": file.name,
        "path": str(file.resolve()),
        "extension": file.suffix,
        "size": file.stat().st_size,
        "created": datetime.fromtimestamp(file.stat().st_ctime),
        "modified": datetime.fromtimestamp(file.stat().st_mtime),
        "sha256": calculate_sha256(file_path),
        "file_type": detect_file_type(file_path)
        
    }

    return file_info