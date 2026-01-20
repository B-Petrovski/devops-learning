import os 
files =os.listdir (".")
print ("Files and their permissions:")
for f in files:
	perms = oct(os.stat(f).st_mode) [-3:]
	print (f"{f}: {perms}")


