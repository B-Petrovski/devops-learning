import os

files = os.listdir (".")
print ("files in current directory:")
for f in files:
        print (f)






import os
files =os.listdir (".")
print ("Files and their permissions:")
for f in files:
        perms = oct(os.stat(f).st_mode) [-3:]
        print (f"{f}: {perms}")
