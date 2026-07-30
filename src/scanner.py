from pathlib import Path
import hashlib
from datetime import datetime

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
        "sha256": calculate_sha256(file_path)
    }

    return file_info