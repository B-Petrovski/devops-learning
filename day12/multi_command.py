import subprocess

commands = [
    ["pwd"],
    ["ls", "-l"],
    ["whoami"],
    ["cat", "nonexistentfile.txt"]  # This will fail
]

for cmd in commands:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Output of {' '.join(cmd)}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Command {' '.join(cmd)} failed with error:\n{e.stderr}")

