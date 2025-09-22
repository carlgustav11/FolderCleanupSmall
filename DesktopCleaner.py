# Tasks to be implemented:
# 1. List all files in a directory using scandir()
# 2. Get the size of a file
# 3. Get the last modified time of a file
# 4. Create folders for each plugin, if they don't already exist
# 5. Move files into their respective folders based on plugin names
# 6. Delete empty folders
# 7. Handle exceptions and errors gracefully
# 8. Log actions taken (e.g., files moved, folders created, errors encountered)

import os
from datetime import datetime

# List all files in a directory using scandir()
basepath = 'c:/Users/admin/Desktop/Rust server mods'

# Function to convert timestamp to human-readable date
def convert_date(timestamp):
    d = datetime.fromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

# Function to list files and their details
def plugin_files(basepath):
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file():
                print(f'File: {entry.name}, Size: {entry.stat().st_size} bytes, Last Modified: {convert_date(entry.stat().st_mtime)}')
            elif entry.is_dir():
                print(f'Directory: {entry.name}')

# Function to create folders for each plugin
def create_plugin_folders(basepath):
    with os.scandir(basepath) as entries:
        for plugin in entries:
            if plugin.is_file():
                folder_path = os.path.join(basepath, f'{plugin.name} folder')
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
                    print(f'Created folder: {folder_path}')
                else:
                    print(f'Folder already exists: {folder_path}')

# Function to move files into their respective folders based on plugin names
def move_files_to_folders(basepath):
    with os.scandir(basepath) as entries:
        for plugin in entries:
            if plugin.is_file():
                folder_path = os.path.join(basepath, f'{plugin.name} folder')
                if os.path.exists(folder_path):
                    new_path = os.path.join(folder_path, plugin.name)
                    os.rename(plugin.path, new_path)
                    print(f'Moved file: {plugin.name} to {folder_path}')
                else:
                    print(f'Folder does not exist for plugin: {plugin.name}')

# Function to delete empty folders
def delete_empty_folders(basepath):
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir():
                if not os.listdir(entry.path):
                    yes = input(f'Are you sure you want to delete the empty folder: {entry.name}? (yes/no): ')
                    if yes.lower() in ['y', 'yes']:
                        os.rmdir(entry.path)
                        print(f'Deleted empty folder: {entry.name}')
                    else:
                        print(f'Skipped deletion of folder: {entry.name}')
                else:
                    print(f'Folder not empty, not deleted: {entry.name}')

# Main execution
if __name__ == "__main__":
    print("Starting desktop cleanup process...")
    plugin_files(basepath)
    print("\nCreating folders...")
    create_plugin_folders(basepath)
    print("\nMoving files...")
    move_files_to_folders(basepath)
    print("\nCleaning up empty folders...")
    delete_empty_folders(basepath)
    print("Desktop cleanup completed!")
