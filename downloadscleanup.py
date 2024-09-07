import os
import shutil
import collections

AUDIO = ['mp3', 'wav', 'raw', 'wma', 'nid', 'midi']
VIDEO = ['mp4', 'mpg', 'mpeg', 'mpv', 'avi', 'mov', 'flv', 'mkv', 'm4v']
IMAGES = ['jpg', 'jpeg', 'png', 'gif', 'svg', 'bmp', 'tif', 'tiff']
DOCUMENTS = ['doc', 'docx', 'pdf', 'xlsx', 'ppt', 'pptx', 'txt', 'csv', 'html', 'log', 'ods', 'tex', 'htm']
COMPRESSED = ['zip', '7z', 'z', 'rar', 'pkg', 'deb', 'gz']
PROGRAM = ['py', 'exe', 'dmg', 'iso', 'dll', 'jar', 'ipynb']

BASE_PATH = os.path.expanduser(r'~/Downloads/')
DEST_DIRECTORY = ['Audio', 'Videos', 'Images', 'Docs', 'Compressed', 'Programs', 'Other']
FOLDERS_DIR = os.path.join(BASE_PATH, 'Folders')

# Create destination directories if they don't exist
for directory in DEST_DIRECTORY:
    directory_path = os.path.join(BASE_PATH, directory)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

# Create the 'folders' directory if it doesn't exist
if not os.path.exists(FOLDERS_DIR):
    os.makedirs(FOLDERS_DIR)

# Process files and folders
files_mapping = collections.defaultdict(list)
files_list = os.listdir(BASE_PATH)

for file_name in files_list:
    file_path = os.path.join(BASE_PATH, file_name)
    if os.path.isdir(file_path):
        # Move directories to the 'folders' directory only if they are not in DEST_DIRECTORY
        if file_name not in DEST_DIRECTORY and file_name != 'Folders':
            shutil.move(file_path, os.path.join(FOLDERS_DIR, file_name))
    elif os.path.isfile(file_path):
        if file_name[0] != '.':
            parts = file_name.split('.')
            file_ext = parts[-1] if len(parts) > 1 else 'no_extension'
            files_mapping[file_ext].append(file_name)

# Move files based on extension
for f_ext, f_list in files_mapping.items():
    if f_ext in AUDIO:
        target_dir = DEST_DIRECTORY[0]
    elif f_ext in VIDEO:
        target_dir = DEST_DIRECTORY[1]
    elif f_ext in IMAGES:
        target_dir = DEST_DIRECTORY[2]
    elif f_ext in DOCUMENTS:
        target_dir = DEST_DIRECTORY[3]
    elif f_ext in COMPRESSED:
        target_dir = DEST_DIRECTORY[4]
    elif f_ext in PROGRAM:
        target_dir = DEST_DIRECTORY[5]
    else:
        target_dir = DEST_DIRECTORY[6]  # "Other" category

    for file in f_list:
        source_path = os.path.join(BASE_PATH, file)
        destination_path = os.path.join(BASE_PATH, target_dir, file)
        os.rename(source_path, destination_path)

print("Files successfully sorted")