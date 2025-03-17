import os
import zipfile

script_directory = os.path.dirname(os.path.abspath(__file__))

root_directory = script_directory

zips_folder = os.path.join(script_directory, "ZIPs")
os.makedirs(zips_folder, exist_ok=True)

processed_dirs = set()

for dirpath, _, filenames in os.walk(root_directory):
    for filename in filenames:
        if filename.endswith(".html"):
            current_dir = os.path.basename(dirpath)
            parent_dir = os.path.basename(os.path.dirname(dirpath))

            if parent_dir and current_dir and dirpath not in processed_dirs:
                processed_dirs.add(dirpath)
                
                zip_name = f"{parent_dir}_{current_dir}.zip"
                zip_path = os.path.join(zips_folder, zip_name)

                with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for root, _, files in os.walk(dirpath):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, dirpath)
                            zipf.write(file_path, arcname)

                print(f"✔ Created: {zip_name} at {zip_path}")
                print(f"✔ Created: {zip_name} at {zip_path}")
