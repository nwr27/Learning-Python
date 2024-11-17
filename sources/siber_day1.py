import json
from datetime import datetime
import os

if not os.path.exists("sources/usspass.json"):
    n = 1
    usspass = {f"try{n}": {"username": None, "password": None, "count": 0, "timestamp": None}}
    with open("sources/usspass.json", "w") as file:
        json.dump(usspass, file)
    print("File created")
    with open("sources/usspass.json", "r") as file:
        usspass = json.load(file)
else:
    with open("sources/usspass.json", "r") as file:
        usspass = json.load(file)
    n = usspass[list(usspass.keys())[-1]]["count"] + 1

print(f"Attempt {n}")
username = input("Enter your username: ")
password = input("Enter your password: ")

usspass[f"try{n}"] = {"username": username, "password": password, "count": n, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

with open("sources/usspass.json", "w") as file:
    json.dump(usspass, file, indent=4)

n += 1
print(usspass)
