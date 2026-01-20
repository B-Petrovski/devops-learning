import os
import shutil

def backup_py_files(source_dir=".", backup_dir="backup_day15"):
    # Create backup folder if it doesn't exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Loop over files in source_dir
    for file in os.listdir(source_dir):
        if file.endswith(".py"):
            src_path = os.path.join(source_dir, file)
            dst_path = os.path.join(backup_dir, file)
            shutil.copy2(src_path, dst_path)
            print(f"Copied {file} to {backup_dir}")

# Run the function
backup_py_files()

