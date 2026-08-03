                    config.json
                        |
                        ▼
                  config.py
             (configuration loader)
                        |
                        ▼
main.py
    |
    ▼
monitor.py
(filesystem event handling)
    |
    ├──────────────┬──────────────┬──────────────┐
    ▼              ▼              ▼              ▼
scanner.py    analyzer.py   quarantine.py   logger.py
(evidence)    (decision)    (response)      (storage)
    |              |              |              |
    ▼              ▼              ▼              ▼
metadata       risk level     move file     save event
SHA256         reasoning      quarantine    history