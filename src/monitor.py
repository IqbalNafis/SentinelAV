from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class SentinelHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print("New file detected:")
            print(event.src_path)

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
