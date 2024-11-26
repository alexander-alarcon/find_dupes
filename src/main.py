#!/usr/bin/env python3

import argparse
import pathlib

from file_hash import find_duplicates
from file_operations import remove_files
from custom_types import HashDict, PathList


def main() -> None:
    """
    Find and remove duplicate files in a given folder.

    Args:
        folder_path (str): Path of the folder to search for duplicates.
    """
    parser = argparse.ArgumentParser(description='Find and remove duplicate files.')
    parser.add_argument(
        'folder_path',
        help='Path of the folder to search for duplicate files.',
        metavar='PATH',
    )
    try:
        args: argparse.Namespace = parser.parse_args()

        folder_path = pathlib.Path(args.folder_path)

        if not folder_path.exists():
            parser.error(f'{folder_path} does not exist.')
        if not folder_path.is_dir():
            parser.error(f'{folder_path} is not a valid directory.')

        hashes: HashDict = {}
        find_duplicates(folder_path, hashes)

        duplicate_groups: list[PathList] = [
            files for files in hashes.values() if len(files) > 1
        ]

        if not duplicate_groups:
            print('No duplicate files found.')
        else:
            print('Duplicate files found:')
            for group in duplicate_groups:
                remove_files(group)
    except KeyboardInterrupt:
        print('\nExiting...')
    except Exception as e:
        print(f'Error: {str(e)}')


if __name__ == '__main__':
    main()
