# Find dupes

## Description

`find_dupes` is a command-line tool that finds and removes duplicate files in a
given directory based on their content, allowing you to maintain a clean file
structure without unnecessary copies of the same files.

## Pre-requisites

Make sure you have installed on your system.

You can verify if Python is installed by running the following command:

```bash
python --version
```

If Python is not installed, you can download it from [python.org](https://www.python.org/) .

## Installation

1. Clone the repository:

```bash
git clone https://github.com/alexander-alarcon/find_dupes.git
```

2. Navigate to the project directory and give execution permissions to the script:

```bash
cd find_dupes
chmod u+x src/main.py
```

## Usage

Once you have the tool installed, you can use it to scan a specified directory
for duplicate files. The basic command syntax is as follows:

```bash
./src/main.py PATH``
```

- Positional arguments:

| Argument | Description                   |
| -------- | ----------------------------- |
| PATH     | Path to the directory to scan |

- Flags:

| Flag     | Default | Description                |
| -------- | ------- | -------------------------- |
| `--help` | `false` | Show help message and exit |

## Examples

1. Finding and removing duplicates in a specific directory:

```bash
./src/main.py example/
```

2. Example output:

```bash
# Duplicate files found:
# [0] - example/file1.txt
# [1] - example/file2.txt
# [2] - example/inner/file3.txt
#
# Enter the index of the file to keep (or type 'all' to delete all duplicates):
```

After displaying the duplicates, you will be prompted to decide which file
to keep or delete. You can either:

- Enter the index of the file to keep.
- Type all to delete all duplicates.

## Additional Notes

- The tool uses file content to identify duplicates, so even if files have
  different names but identical contents, they will be considered duplicates.
- Make sure to review the files listed as duplicates before deleting them
  to avoid unintentional data loss.
