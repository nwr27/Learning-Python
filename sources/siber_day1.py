import json
from datetime import datetime
import os

my_username = "nana"
my_password = "wartana"
my_ip = "192.168.240.131"
ip_block_list = []
block_times = {}


if not os.path.exists("sources/siber_test1_database/usspass.json"):
    os.makedirs("sources/siber_test1_database", exist_ok=True)
    n = 1
    usspass = {f"try{n}": {"ip": my_ip, "username": None, "password": None, "count": 0, "timestamp": None}}
    with open("sources/siber_test1_database/usspass.json", "w") as file:
        json.dump(usspass, file)
    print("File created")
    with open("sources/siber_test1_database/usspass.json", "r") as file:
        usspass = json.load(file)
else:
    with open("sources/siber_test1_database/usspass.json", "r") as file:
        usspass = json.load(file)
    n = usspass[list(usspass.keys())[-1]]["count"] + 1

print(f"Attempt {n}")
username = input("Enter your username: ")
password = input("Enter your password: ")

usspass[f"try{n}"] = {"ip": my_ip, "username": username, "password": password, "count": n, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

with open("sources/siber_test1_database/usspass.json", "w") as file:
    json.dump(usspass, file, indent=4)

if my_ip in ip_block_list:
    print("Your IP has been blocked")
    exit()
else:
    if usspass[f"try{n}"]["username"] == my_username and usspass[f"try{n}"]["password"] == my_password:
        print("Login successful")
        # block_times[my_ip] = 0
    else:
        print("Login failed")
        # block_times[my_ip] += 1
        # if block_times[my_ip] >= 3:
        #     print("You have been tried 3 times, your IP has been blocked")
        #     ip_block_list.append(my_ip)
    n += 1
