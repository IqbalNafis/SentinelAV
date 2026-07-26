# Development Log

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
