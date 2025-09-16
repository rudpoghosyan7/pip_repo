import subprocess

services = ["notepad.exe", "explorer.exe"]  # test with common processes

for svc in services:
    result = subprocess.run(["tasklist"], capture_output=True, text=True)
    if svc.lower() in result.stdout.lower():
        print(f"✅ {svc} is running")
    else:
        print(f"❌ {svc} is NOT running")
