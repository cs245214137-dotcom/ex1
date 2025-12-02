import subprocess

# Run a simple command: list files in current directory
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

# Print output
print("STDOUT:\n", result.stdout)
print("STDERR:\n", result.stderr)
