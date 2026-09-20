# task3_move_jpg_files.py
# CodeAlpha Python Task 3: Task Automation
# Moves all .jpg files from a source folder into a new folder.

import os
import shutil


def move_jpg_files(source_folder, destination_folder):
    """Moves every .jpg/.jpeg file from source_folder to destination_folder."""

    if not os.path.isdir(source_folder):
        print(f"Source folder not found: {source_folder}")
        return

    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    moved_count = 0

    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".jpg", ".jpeg")):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Avoid overwriting a file that already has the same name
            if os.path.exists(destination_path):
                name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(destination_path):
                    destination_path = os.path.join(
                        destination_folder, f"{name}_{counter}{ext}"
                    )
                    counter += 1

            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
            moved_count += 1

    if moved_count == 0:
        print("No .jpg files found.")
    else:
        print(f"\nDone! {moved_count} file(s) moved to '{destination_folder}'.")


def main():
    source = input("Enter the source folder path: ").strip().strip('"')
    destination = input("Enter the new folder name/path for the images: ").strip().strip('"')
    move_jpg_files(source, destination)


if __name__ == "__main__":
    main()
