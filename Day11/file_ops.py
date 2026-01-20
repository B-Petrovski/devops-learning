import shutil
import os 

#make sure this file exists
source_file = "hello_devops.py"
destination_file = "hello_devops_copy.py"

#copy the file

shutil.copy(source_file, destination_file)
print (f"Copied {source_file} to {destination_file}")

#create a folder if it does't exist

os.makedirs ('backup', exist_ok=True)

# Move the copy into backup folder
shutil.move(destination_file, "backup/" + destination_file)

print (f"Moved {destination_file} to backup folder")

