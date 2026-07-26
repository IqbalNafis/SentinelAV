from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from scanner import scan_file
from reporter import display_report
from analyzer import analyze_file
import time

class SentinelHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print("\nNew file detected!")
            file_info = scan_file(event.src_path)
            analysis = analyze_file(file_info)
            display_report(file_info, analysis)

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
