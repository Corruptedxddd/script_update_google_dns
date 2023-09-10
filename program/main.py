#CHEESEBALLSVK/CORRUPTED DID THIS SCRIPT <3
import requests
from requests import get
import time
#CHECK FIRST STARTUP
with open('first_start.txt', 'r') as file:
    file_contents_startup = file.read()
#print(file_contents_startup)

#FIRST START UP SEQUENCE
if(file_contents_startup=="0"):
    with open("username.txt", "w") as file:
        pass
    with open("password.txt", "w") as file:
        pass
    with open("domain.txt", "w") as file:
        pass
    with open("old_ip.txt", "w") as file:
        pass
    print("OW... Welcome - this is your first time using this script")
    time.sleep(1)
    print("Initial Startup starting ...")
    time.sleep(1)
    user_name = input("Please enter username of dynamic DNS: ")
    password = input("Please enter password of dynamic DNS: ")
    domain = input("Please enter domain which we are using for this script (subdomain.domain.com): ")
    print("Getting your IP address ...")
    time.sleep(1)
    ip = get('https://api.ipify.org').content.decode('utf8')
    print('Your public IP address is: {}'.format(ip))
    url = f'https://{user_name}:{password}@domains.google.com/nic/update?hostname={domain}&myip={ip}'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Failed to retrieve the URL. Status code: {response.status_code}")

    #write everthing
    with open("first_start.txt", "w") as file:
        file.write("1")
    with open("username.txt", "w") as file:
        file.write(user_name)
    with open("password.txt", "w") as file:
        file.write(password)
    with open("domain.txt", "w") as file:
        file.write(domain)
    with open("old_ip.txt", "w") as file:
        file.write(ip)
else:

    ip = get('https://api.ipify.org').content.decode('utf8')
    with open('old_ip.txt', 'r') as file:
        file_contents_old_ip = file.read()
    if file_contents_old_ip == ip:
        print("Nothing has changed (if something went wrong change 0 instead of 1 in first_start.txt)")
    else:
        print("IP WAS CHANGED")
        with open("username.txt", "r") as file:
            file_contents_username = file.read()
        with open("password.txt", "r") as file:
            file_contents_password = file.read()
        with open("domain.txt", "r") as file:
            file_contents_domain = file.read()
        url = f'https://{file_contents_username}:{file_contents_password}@domains.google.com/nic/update?hostname={file_contents_domain}&myip={ip}'
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Failed to retrieve the URL. Status code: {response.status_code}")
        with open("old_ip.txt", "w") as file:
            file.write(ip)
#CHEESEBALLSVK/CORRUPTED DID THIS SCRIPT <3