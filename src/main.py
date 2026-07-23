from monitor import start_monitoring

def main():
    print("SentinelAV starting...")
    folder = "monitored"

    start_monitoring(folder) 

if __name__ == "__main__":
    main()