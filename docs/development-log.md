SentinelAV Development Log
23 July 2026 — Project Initialization and Development Environment Setup
Repository Creation

Created the initial SentinelAV GitHub repository and established the project structure:

sentinelAV/
├── database/
├── docs/
├── quarantine/
├── reports/
├── src/
└── tests/

The initial folder structure was designed to separate:

Documentation
Source code
Testing
Future database and quarantine functionality
Generated reports
Documentation Layer Setup

Created the initial documentation structure:

docs/
├── project-overview.md
├── architecture.md
└── development-log.md

Documentation responsibilities:

project-overview.md
Defines SentinelAV's purpose, goals, scope, and development status.
architecture.md
Describes the system design, module relationships, and future data flow.
development-log.md
Records implementation progress, troubleshooting, decisions, and lessons learned.
Python Environment Setup

Created a Python virtual environment using:

python -m venv venv

The command completed successfully without output. The generated venv directory confirmed successful creation.

Attempted to activate the environment:

venv/Scripts/activate

Encountered PowerShell execution policy restrictions:

running scripts is disabled on this system
Resolution

Updated the execution policy for the current user:

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

Successfully activated the virtual environment:

(venv) PS C:\Users\TUF A16\Documents\sentinelAV>

Verified Python was using the virtual environment:

where.exe python

Result:

sentinelAV\venv\Scripts\python.exe
Initial Python Program

Created the first SentinelAV executable entry point:

src/main.py

Initial purpose:

Confirm Python execution
Establish the application entry point

First successful output:

SentinelAV starting...
System monitoring initialized.
Issue Encountered

The first version of main.py contained incorrect indentation:

def main():
    ...
    if __name__ == "__main__":
        main()

The entry condition was placed inside the function.

Resolution

Corrected the structure:

def main():
    print("SentinelAV starting...")
    print("System monitoring initialized.")


if __name__ == "__main__":
    main()
Lesson Learned

Python indentation defines program structure. Incorrect indentation can change execution behavior without necessarily generating a syntax error.

24 July 2026 — Filesystem Monitoring Module
Objective

Implement SentinelAV's first security capability:

Detect when a new file appears inside a monitored directory.

The monitoring system was designed as the first stage of the SentinelAV pipeline:

Observe → Analyze → Assess → Report
Dependency Installation

Installed the filesystem monitoring library:

pip install watchdog

Saved dependencies:

pip freeze > requirements.txt
Monitor Module Implementation

Created:

src/monitor.py

Implemented:

FileSystemEventHandler
Observer
Directory monitoring

Created a testing directory:

monitored/

The system was connected through:

main.py
    |
    v
monitor.py
Filesystem Event Debugging
Issue Encountered

Initial implementation used:

on_modified()

This monitored changes to existing files instead of detecting newly created files.

Expected behavior:

Detect newly introduced files

Actual behavior:

React only when existing files changed
Resolution

Changed the event handler to:

on_created()

Final behavior:

When a new file is created inside the monitored directory:

Example:

hello.txt

SentinelAV detects:

New file detected:
C:\Users\TUF A16\Documents\sentinelAV\monitored\henlo.txt

Current Development Status

SentinelAV prototype currently supports:

Project structure
Documentation framework
Python development environment
Git version control workflow
Filesystem monitoring
Detection of newly created files

Next Development Goals
Implement file metadata extraction
Filename
Extension
File size
Creation timestamp
Generate cryptographic hashes
SHA256 identification
Create basic risk analysis logic
Develop reporting system
Implement quarantine functionality
