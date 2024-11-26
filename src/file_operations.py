import pathlib

from custom_types import PathList, UserResponse


def remove_files(path_list: PathList) -> None:
    """
    Removes duplicate files from a list of file paths.

    Args:
        path_list (PathList): A list of file paths.
    """
    if not path_list:
        print('No files to remove.')
        return

    print('\nDuplicate files found:')
    for index, file in enumerate(path_list):
        size = file.stat().st_size
        print(f'[{index}] - {file} (Size: {size / (1024 * 1024):.2f} MB)')

    file_to_keep: pathlib.Path | None = None

    try:
        keep_file = (
            input(
                "\nEnter the index of the file to keep (or type 'all' to delete all duplicates): "
            )
            .strip()
            .lower()
        )

        match keep_file:
            case UserResponse.ALL:
                confirmation_message = (
                    'Are you sure you want to delete all duplicates? (yes/no/cancel): '
                )
            case _:
                try:
                    keep_file_index = int(keep_file)
                    if keep_file_index < 0 or keep_file_index >= len(path_list):
                        print('Invalid index.')
                        return
                    file_to_keep = path_list[keep_file_index]
                    confirmation_message = f"Are you sure you want to delete all duplicates except '{file_to_keep}'? (yes/no/cancel): "
                except ValueError:
                    print('Invalid input. Please enter a valid index.')
                    return

        confirmation: UserResponse | None = None
        while confirmation not in [
            UserResponse.YES,
            UserResponse.NO,
            UserResponse.CANCEL,
        ]:
            confirmation_input = input(confirmation_message).strip().lower()

            try:
                confirmation = UserResponse(confirmation_input)
            except ValueError:
                print("Invalid input. Please enter 'yes', 'no', or 'cancel'.")

        match confirmation:
            case UserResponse.YES:
                deleted_files = 0
                for file in path_list:
                    if keep_file.lower() == 'all' or file != file_to_keep:
                        file.unlink()
                        print(f"Removed '{file}'")
                        deleted_files += 1
                print(f'\n{deleted_files} duplicate files were removed.')
            case UserResponse.NO:
                print('No files were deleted.')
            case UserResponse.CANCEL:
                print('Operation cancelled. No files were deleted.')

    except ValueError:
        print("Invalid input. Please enter a valid index or 'all'.")
