import pathlib
import hashlib

from custom_types import HashDict, PathList


def hash_file(file_path: pathlib.Path) -> str:
    """
    Compute the SHA1 hash of a file.

    Args:
        file_path (pathlib.Path): The path to the file to be hashed.

    Returns:
        str: The hexadecimal representation of the computed hash, empty string if an error occurs.

    Raises:
        FileNotFoundError: If the file is not found.
        PermissionError: If the file cannot be read due to permissions.
        Exception: If there is an error while hashing the file.
    """
    try:
        hasher = hashlib.sha1()
        with open(file_path, 'rb') as f:
            while True:
                data: bytes = f.read(1024)
                if not data:
                    break
                hasher.update(data)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f'File not found: {file_path}')
        return ''
    except PermissionError:
        print(f'Permission denied: {file_path}')
        return ''
    except Exception as e:
        print(f'Error hashing file {file_path}: {str(e)}')
        return ''


def add_hash_to_dict(file_path: pathlib.Path, hashes: HashDict) -> None:
    """
    Add the hash of a file to a dictionary of hashes and file paths.

    Args:
        file_path (pathlib.Path): The path to the file.
        hashes (HashDict): A dictionary containing hashes of files as keys and a list of file paths as values.
    """
    try:
        hashed_file: str = hash_file(file_path)
        if hashed_file:
            if hashed_file not in hashes:
                hashes[hashed_file] = [file_path]
            else:
                hashes[hashed_file].append(file_path)
    except Exception as e:
        print(f'Error hashing file {file_path}: {str(e)}')


def find_duplicates(folder_path: pathlib.Path, hashes: HashDict) -> PathList:
    """
    Find duplicates in a given folder path by comparing hashes of the files.

    Args:
        folder_path (pathlib.Path): The path to the folder to search for duplicates.
        hashes (HashDict): A dictionary containing hashes of files as keys and a list of file paths as values.

    Returns:
        PathList: A list of file paths that are duplicates.
    """
    duplicates: PathList = []

    for file in folder_path.rglob('*'):
        if file.is_file():
            add_hash_to_dict(file, hashes)

    return duplicates
