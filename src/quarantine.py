from pathlib import Path
import shutil
from datetime import datetime

def quarantine_file(file_path, reason):
    """
    Move a suspicious file into to the quarantine folder.
    """
    source = Path(file_path)
    destination = Path("quarantine") / source.name

    shutil.move(str(source), str(destination))

    print(f"\nFile quarantined:")
    print(destination)  

    print(f"Reason : {reason}")
    print(f"Time   : {datetime.now()}")
