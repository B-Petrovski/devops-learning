import os

def list_python_filles(directory="."):
	files = [f for f in os.listdir(directory) if f.endswith(".py")]
	for file in files:
		print(file)

list_python_filles()

