import requests
import json
import os
import time

print(" \n### STOP TUNNEL ###")
os.system("wg-quick down ./tunnel.conf")
time.sleep(1)

print(" \n### CREATE NEW TUNNEL ###")
os.system("curl https://tunnel.pyjam.as/80 > tunnel.conf && wg-quick up ./tunnel.conf")
time.sleep(1)

print(" \n### FIND NEW public url ###")
#find public url in tunnel.conf
n_line = 5
file = open("tunnel.conf", "r")
for x in range(n_line):
    url = file.readline()
start_url = url.find("on ")
end_url = url.find("\n")
url = url[start_url+3:end_url-5]
print("new public url: " + url)
url = url + "/citovoip/"
print("citovoip url: " + url)

print(" \n### UPDATE REDIRECT URL ###")
new_url = requests.get("http://teleprojects.altervista.org/user1_update.php?url=" + url)
if new_url.status_code == 200:
    print("Update OK!")
else:
    print("Update error, error code: " + new_url.status_code)    




    
# sudo apt install python3-pip
#  python3 -m pip install requests