# Development Log

## 23 July 2026

### Completed

- Created SentinelAV GitHub repository
- Configured Git environment
- Created initial project structure
- Added documentation directory

### Lessons Learned

- Git tracks changes through commits
- Empty folders require placeholder files
- Software projects benefit from planning before implementation

## 24 July 2026
## Current Development Status 

SentinelAV is currently in the prototype development phase.

Completed:
- Project structure and documentation setup
- Python development environment configuration
- Filesystem monitoring module
- Detection of newly created files in monitored directories

Current Focus:
- File metadata extraction
- File type identification
- Cryptographic hash generation
- Basic risk assessment

Future Development:
- Suspicious behavior analysis
- Quarantine functionality
- Security report generation
- Graphical user interface


## 26 July 2026
## Current Features

### File Monitoring
SentinelAV monitors a designated directory and detects newly created files using filesystem event monitoring.

### File Metadata Collection
The scanner module collects:
- Filename
- File path
- File extension
- File size
- Creation timestamp
- Modification timestamp
- SHA256 hash

### Risk Analysis
The analyzer module performs basic rule-based assessment based on file extensions.

Currently monitored file types:
- .exe
- .bat
- .cmd
- .ps1
- .zip
- .rar
- .7z

### 30/7/2026
SentinelAV has successfully implemented a real-time filesystem monitoring pipeline.

Current capabilities:

- Monitors the Windows Downloads folder in real time
- Detects newly created files using filesystem events
- Extracts file metadata:
  - Filename
  - File path
  - Extension
  - File size
  - Creation and modification timestamps
- Generates SHA256 file hashes for identification
- Performs basic rule-based risk analysis
- Generates human-readable scan reports
- Filters temporary download files such as `.tmp`, `.crdownload`, and `.part`
- Saves scan results into a persistent scan history log

### Next Steps

- Improve scan history formatting
- Add file quarantine functionality
- Implement persistent threat database
- Improve risk scoring system
- Develop user notifications

###31/7/2026
- Automatically quarantines high-risk files
- Records quarantine actions with detection reasons

