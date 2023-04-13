import os
import time
import subprocess
import time
import hashlib

start = time.ctime(time.time())
print("Start time:", start)
pwd_file = open("PwnedPWs100k", encoding="utf8")
pwds = [line.rstrip('\n') for line in pwd_file]
gng_file = open("gang", encoding="utf8")
gng_names = [line.rstrip('\n') for line in gng_file]
slt_file = open("SaltedPWs", encoding="utf8")
slts = [tuple(line.rstrip('\n').split(",")) for line in slt_file]
# hashes with gang member names
gng_slts = []
for slt in slts: 
    if slt[0] in gng_names: 
        gng_slts.append(slt)
# Hash function
def hashF(password):
    hash = hashlib.sha256()
    hash.update(bytes(password, 'utf-8'))
    hashed = hash.hexdigest()
    return hashed

def _break():
    for pwd in pwds:
        #add two digit number to the end
        for i in range(0,10):
            #print(hashed_pass)
            for gang_salt in gng_slts:
                new_pass = pwd + str(i)
                # hash the password in sha256
                salted_pass = hashF(gang_salt[1] + new_pass)
                #if hashes match
                if (salted_pass == gang_salt[2]):
                    output = subprocess.run(["python3", "Login.pyc", gang_salt[0], new_pass], capture_output = True, text = True).stdout.strip("\n")
                    if "success" in output:
                        print("The Working Password For", gang_salt[0], "is", new_pass)
                        end = time.ctime(time.time())
                        print("End time:", end)
                        break
_break()