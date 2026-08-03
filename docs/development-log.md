# Development Log

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
