import subprocess

result = subprocess.run(
    ["docker", "ps", "-a"],
    capture_output=True,
    text=True
)

print("RETURN CODE:", result.returncode)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print(result.stdout)
