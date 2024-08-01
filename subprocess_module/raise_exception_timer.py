import subprocess

completed_process = subprocess.run(["python","timer.py","ten"],check=True)
print(f"Return codec : {completed_process.returncode}")
print(f"Args : {completed_process.args}")

