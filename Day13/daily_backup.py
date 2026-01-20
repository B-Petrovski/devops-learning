import shutil
import os

#create the backup folder is it doesn't exist
backup_folder = "daily_backup"
os.makedirs(backup_folder, exist_ok=True)

#Get all .py files in the current directory
py_files = [f for f in os.listdir() if f.endswith('.py')]

#copy each .py file into the backup folder
for file in py_files:
	shutil.copy(file, os.path.join(backup_folder, file))
	print (f"Copied {file} to {backup_folder}")

