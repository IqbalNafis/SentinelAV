from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from scanner import scan_file
from reporter import display_report
from analyzer import analyze_file
from logger import save_log
from quarantine import quarantine_file
from config import load_config
import time

TEMP_EXTENSIONS = [ ".tmp", ".crdownload", ".part" ]
class SentinelHandler(FileSystemEventHandler):
    def process_file(self, file_path, event_type):
        print(f"\n{event_type} detected!")

        file_info = scan_file(file_path)

        if file_info is None:
            print("File unavailable, skipping scan.")
            return
        analysis = analyze_file(file_info)

        risk_levels = {
            "LOW": 1,
            "MEDIUM": 2,
            "HIGH": 3
        }

        file_risk = risk_levels[analysis["risk"]]
        threshold = risk_levels[self.config["risk_threshold"]]

        if file_risk >= threshold and self.config["auto_quarantine"]:
            quarantine_file(file_path, analysis["reason"])
            action = "Quarantined"
        elif file_risk >= threshold:
            action = "Detected - Not Quarantined"
        else: 
            action = "Allowed"
        display_report(file_info, analysis, action)
        save_log(file_info, analysis, action, self.config["log_file"])

    def __init__(self):
        super().__init__()
        self.config = load_config()

    def on_created(self, event):
        if event.is_directory:
            return

        if any(event.src_path.endswith(ext) for ext in TEMP_EXTENSIONS):
            print(f"Temporary file detected: {event.src_path}, skipping scan.")
            return

        self.process_file(event.src_path, "New file")
        

    def on_moved(self, event):
        if event.is_directory:
            return

        if any (event.dest_path.endswith(ext) for ext in TEMP_EXTENSIONS):
            print(f"Temporary file detected: {event.dest_path}, skipping scan.")
            return
        
        self.process_file(event.dest_path, "File moved/renamed")
        
def start_monitoring(path):
    event_handler = SentinelHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)

    observer.start()

    print("Monitoring started on path:")
    print(f"Watching: {path}")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()
