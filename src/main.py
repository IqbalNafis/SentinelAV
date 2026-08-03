from monitor import start_monitoring
from pathlib import Path
from config import load_config
def main():
    print("SentinelAV starting...")
    
    config = load_config()
    folder = config["monitor_folder"]

    start_monitoring(folder) 

if __name__ == "__main__":
    main()