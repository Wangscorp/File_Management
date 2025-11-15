# File Management and Data Processing Utility

A comprehensive Python project demonstrating file management, logging, backup operations, and data processing with JSON and CSV handling.

## Project Overview

This utility assists users in creating, backing up, organizing, logging, and analyzing data files. It integrates multiple Python modules for file handling and system operations.

## Files Included

1. **file_manager.py** - Main script containing Tasks 1-6
2. **students_report.py** - Data processing script for Task 7
3. **students.json** - Sample JSON data for testing
4. **README.md** - This file

## Tasks Implemented

### Tasks 1-6: File Manager (file_manager.py)

- **Task 1**: Project Initialization - Creates and displays StudentFiles folder
- **Task 2**: File Creation - Accepts student names and creates dated file
- **Task 3**: File Information - Displays file contents, size, and modification date
- **Task 4**: Backup and Archiving - Creates backup and manages Archive folder
- **Task 5**: Logging System - Records all activities with timestamps
- **Task 6**: Advanced Operations - Allows file deletion and listing

### Task 7: Data Processing (students_report.py)

- Reads student data from JSON file
- Calculates average scores for each student
- Generates CSV report sorted by average (descending)
- Includes error handling for missing files

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## How to Run

### For Tasks 1-6:
\`\`\`bash
python file_manager.py
\`\`\`

Follow the prompts to:
1. Input five student names
2. Choose whether to delete files
3. Review activity logs

### For Task 7:
\`\`\`bash
python students_report.py
\`\`\`

This will read `students.json` and generate `report.csv` in the current directory.

### Run Both Tasks:
\`\`\`bash
python file_manager.py
python students_report.py
\`\`\`

## Project Output

After running, you'll have:

\`\`\`
StudentFiles/
  ├── records_YYYY-MM-DD.txt
  ├── activity_log.txt
  └── Archive/
      └── backup_records_YYYY-MM-DD.txt

report.csv (generated from Task 7)
\`\`\`

## Code Features

- **Modular Design**: Each task is implemented as a separate function
- **Error Handling**: Comprehensive try-except blocks with graceful exits
- **Logging**: All activities are timestamped and recorded
- **User Input Validation**: Handles empty or invalid entries
- **Clear Output**: Descriptive messages guide users through each step

## Module Usage

- **os**: File/folder creation and manipulation
- **sys**: Program exit handling
- **shutil**: File copying and moving
- **datetime**: Timestamps and date formatting
- **json**: Reading JSON data
- **csv**: Writing CSV reports

## Notes

- The activity log accumulates over multiple runs
- Backup files are automatically archived
- CSV reports are sorted by average score in descending order
- All timestamps follow YYYY-MM-DD HH:MM:SS format

## Author Notes

This project demonstrates best practices in:
- File I/O operations
- Exception handling
- Modular programming
- Data processing
- Logging and monitoring
