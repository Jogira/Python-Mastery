import subprocess

completed = subprocess.run(["python3", "subprocess.py"], shell=True)
print(type(completed))
print("args", completed.args)
print("returncode", completed.args)
print("stderr", completed.args)
print("stdout", completed.args)
