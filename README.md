# Asynchronous programming in Python

# Async File Sorter

An asynchronous Python script for sorting files by their extensions with logging console output.

## Description

This script recursively scans a given source directory and copies all found files into a new destination folder, organizing them into subfolders based on their file extensions. It leverages asynchronous file operations (`aiopath`, `aioshutil`) and structured logging.

## Features

- Asynchronous recursive folder traversal
- File copying into folders grouped by extension
- Logging to multiple outputs:
- `file_sorting.log` — logs `DEBUG` level messages
- Console output

## Requirements

- Python 3.10+
- `aiopath`
- `aioshutil`

Install dependencies:

```
pip install aiopath aioshutil

```

## Usage

python sorting_files.py <source_folder> <destination_folder>

Example:
python sorting_files.py "F:\Projects\Downloads" "F:\Projects\SortedFiles"

Project Structure

```
project_root/
├── file_sorting/
│   └──logging_config.py
├── sorting_files.py
├── sorting.log
├── README.md
└── requirements.txt
```
