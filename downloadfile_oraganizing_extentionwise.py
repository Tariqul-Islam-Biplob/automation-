import os
import shutil

download_path = r"C:\Users\Biplob\Downloads"

for filename in os.listdir(download_path):
    full_path = os.path.join(download_path, filename)

    if os.path.isdir(full_path):
        continue

    name, ext = os.path.splitext(filename)

    if not ext:
        continue

    ext_folder = ext[1:].upper()  # ✅ add () to call the function
    target_folder = os.path.join(download_path, ext_folder)

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    new_location = os.path.join(target_folder, filename)
    shutil.move(full_path, new_location)
    print(f"Moved {filename} to {ext_folder}/")
