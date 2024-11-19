import subprocess

def install_packages():
    packages = ["wget", "curl", "build-essential"]
    for package in packages:
        subprocess.run(["sudo", "apt-get", "install", "-y", package])
    print("Packages installed successfully.")
