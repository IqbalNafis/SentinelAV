from monitor import start_monitoring
from pathlib import Path

def main():
    print("SentinelAV starting...")
    
    folder = Path.home() / "Downloads"

    start_monitoring(folder) 

if __name__ == "__main__":
    main()