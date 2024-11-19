import subprocess

def install_packages():
    packages = ["curl", "wget"]
    for package in packages:
        subprocess.run(["sudo", "apt-get", "install", "-y", package])
    print("Packages installed successfully.")
