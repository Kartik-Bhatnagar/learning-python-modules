import subprocess
print("!! Starting to execute the command with timeout")
print(subprocess.run(["python","timer.py","4"],timeout=2))
print("!!Command executed with timeout")
