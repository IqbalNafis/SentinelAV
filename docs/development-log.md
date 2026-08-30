# Development Log

## 30 August 2026

### Completed

* Added file readiness handling to reduce scanning failures when newly created files are temporarily unavailable.
* Added file signature detection using magic bytes.
* SentinelAV can now identify several file types based on file contents rather than relying solely on file extensions.
* Added extension and detected-file-type mismatch detection.
* Expanded filesystem monitoring to detect moved and renamed files using `on_moved()`.
* Refactored file processing into a reusable `process_file()` pipeline to avoid duplicating scanning, analysis, quarantine, reporting, and logging logic.

### Testing

* Verified normal file detection and scanning.
* Verified PDF, image, and executable file-type identification.
* Successfully tested renamed/moved files.
* Successfully demonstrated detection of a file whose extension did not match its detected file type.
* Identified a known edge case where copying a file within the monitored directory can trigger a scan before Windows has finished making the copied file accessible, resulting in a temporary `PermissionError`.

### Current Limitations

* File-copy race conditions may still cause a temporary scanning failure.
* `on_modified()` monitoring has not yet been implemented.
* Risk assessment remains primarily rule-based and will be improved in a future development session.

### Next Steps

* Improve the risk assessment engine.
* Introduce multiple evidence-based indicators into risk decisions.
* Improve the explanation of detection evidence in scan reports.
* Continue strengthening SentinelAV's detection and response capabilities.

## 3 August 2026 — Configuration Layer Implementation

Implemented external configuration management.

Changes:
- Added config.json for centralized settings
- Added config.py loader module
- Connected monitoring system to configuration values
- Added configurable auto quarantine behaviour
- Added configurable risk threshold policy
- Added configurable log file destination

SentinelAV can now operate with adjustable security settings instead of fixed code behavior.

## 31 July 2026 — Quarantine Response System

#### Quarantine System

Implemented a quarantine module that moves high-risk files into a dedicated quarantine directory.

Features:

- Automatic isolation of HIGH-risk files
- Prevents suspicious files from remaining in monitored locations
- Records quarantine actions in scan history

### Improvements

Added quarantine metadata:

- Detection reason
- Timestamp of quarantine action

### Updated Workflow

SentinelAV now follows:

Detection → Analysis → Decision → Quarantine → Logging

### Current Status

SentinelAV can detect, analyze, isolate, and record suspicious files in real time.

## 30 July 2026 — Real-time Monitoring and Scan Logging

### Objective

Upgrade SentinelAV from a controlled testing environment into a practical endpoint monitoring prototype.

### Completed Work

#### Downloads Folder Monitoring

- Replaced the test `monitored/` directory with the user's Windows Downloads folder.
- SentinelAV now observes real filesystem activity using Watchdog events.

### Improvements

#### Temporary File Handling

During testing, browser downloads were detected as temporary files such as:

- `.tmp`
- `.crdownload`
- `.part`

Added filtering logic to prevent unnecessary scanning of incomplete downloads.

### Scan Logging System

Implemented `logger.py`.

SentinelAV now creates persistent records inside:

reports/scan_history.log


Each scan records:

- Timestamp
- Filename
- Extension
- File size
- SHA256 hash
- Risk assessment
- Detection reason

### Testing

Successfully tested:

- PDF download detection
- Temporary file filtering
- Manual `.exe` creation
- High-risk classification
- Log generation

### Current Status

SentinelAV can now monitor real user activity, analyze new files, and preserve security events for future review.

### Next Development Goal

Implement a quarantine system that can isolate suspicious files.

## Phase 1: Project Initialization

### Repository Setup
- Created SentinelAV GitHub repository
- Established project structure:
  - src/
  - docs/
  - tests/
  - reports/
  - quarantine/

### Environment Setup
- Created Python virtual environment
- Installed required dependencies
- Configured Git tracking

---

## Phase 2: File Monitoring Module

Implemented filesystem monitoring using watchdog.

Features:
- Detect newly created files
- Monitor selected directory
- Trigger scanning pipeline

---

## Phase 3: File Scanner Module

Created scanner.py.

Implemented:
- File metadata extraction
- SHA256 hash generation
- Timestamp collection

Security concepts learned:
- Cryptographic hashing
- File fingerprinting
- Metadata analysis

---

## Phase 4: Reporting Module

Created reporter.py.

Implemented:
- Human-readable scan reports
- Structured output formatting

---

## Phase 5: Basic Risk Analyzer

Created analyzer.py.

Implemented:
- Extension-based risk classification
- Detection of potentially sensitive file types

Current rules:
- Executables/scripts → HIGH risk
- Archives → MEDIUM risk
- Other files → LOW risk
