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
hsh_file = open("HashedPWs", encoding="utf8")
hshs = [tuple(line.rstrip('\n').split(",")) for line in hsh_file]
# hashes with gang member names
gng_hshs = []
for hsh in hshs: 
    if hsh[0] in gng_names: 
        gng_hshs.append(hsh)
# Hash function
def hashF(password):
    hash = hashlib.sha256()
    hash.update(bytes(password, 'utf-8'))
    hashed = hash.hexdigest()
    return hashed

def _break():
    for pwd in pwds:
        #add two digit number to the end
        for i in range(10,100):
            pass_nums = pwd + str(i)
            # hash the password in sha256
            hashed_pass = hashF(pass_nums)
            #print(hashed_pass)
            for gang_hash in gng_hshs:
                #if hashes match
                if (hashed_pass == gang_hash[1]):
                    output = subprocess.run(["python3", "Login.pyc", gang_hash[0], pass_nums], capture_output = True, text = True).stdout.strip("\n")
                    if "success" in output:
                        print("The Working Password For", gang_hash[0], "is", pass_nums)
                        end = time.ctime(time.time())
                        print("End time:", end)
                        break
_break()
