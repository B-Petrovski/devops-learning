import subprocess

# Run 'ls -l' command
result = subprocess.run(["ls"], capture_output=True, text=True)
print("Output of ls")
print(result.stdout)
