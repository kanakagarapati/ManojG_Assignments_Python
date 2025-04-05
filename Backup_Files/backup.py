import os
import shutil
import datetime

def backup_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Destination folder '{destination_folder}' created.")

    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)

        if os.path.isfile(source_file):
            if os.path.exists(destination_file):
                print(f"File '{filename}' already exists in the destination folder.")
                destination_file = destination_file + f"_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
                destination_file += os.path.splitext(filename)[1]
                shutil.copy2(source_file, destination_file)
                print(f"File '{filename}' As already exists in the destination folder created file with time stamp.")
            else:
                shutil.copy2(source_file, destination_file)
                print(f"File '{filename}' backed up successfully.")

if __name__ == "__main__":
    source_folder = input("Enter the source folder path: ").strip()
    destination_folder = input("Enter the destination folder path: ").strip()
    backup_files(source_folder, destination_folder)