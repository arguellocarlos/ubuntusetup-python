import os
import shutil
import psutil
import time
import subprocess
import distro
from user_setup import add_new_user
from package_install import install_packages

def check_ubuntu_version():
    version = distro.linux_distribution(full_distribution_name=False)[1]
    print(f"Ubuntu Version: {version}")

def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    print(f"Disk Space Available: {free // (2**30)} GB")

def check_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_string = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
    print(f"Uptime: {uptime_string}")

def check_free_memory():
    memory = psutil.virtual_memory()
    print(f"Free Memory (RAM): {memory.available // (2**20)} MB")

def check_cpu_load():
    load = os.getloadavg()
    print(f"CPU Load: {load}")

def print_ascii_art():
    art = """
   +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
   |U|b|u|n|t|u| |P|o|s|t| |I|n|s|t|a|l|l|a|t|i|o|n| |S|c|r|i|p|t|
   +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
    """
    print(art)

def menu():
    print("Ubuntu Post Installation Script...")
    print("1. Add a new user with sudo privilege...")
    print("2. Install Packages...")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        add_new_user()
    elif choice == "2":
        install_packages()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    # Prompt for sudo password at the beginning
    subprocess.run(["sudo", "-v"])
    
    print_ascii_art()
    menu()
    check_ubuntu_version()
    check_disk_space()
    check_uptime()
    check_free_memory()
    check_cpu_load()
