import json
from datetime import datetime
import os


class User:
    def __init__(self, my_username="admin", my_password="admin", my_ip="admin"):
        self.username = None
        self.password = None
        self.my_username = my_username
        self.my_password = my_password
        self.my_ip = my_ip
        self.count = 1
        self.success = False

    def login(self):
        global usspass, main_path
        main_path = "sources/siber_test1_database"
        os.makedirs(main_path, exist_ok=True)
        file_name = "usspass.json"
        file_path = os.path.join(main_path, file_name)
        if not os.path.exists(file_path):
            usspass = {}
        else:
            with open(file_path, "r") as file:
                usspass = json.load(file)
        print(f"Attempt {self.count}")
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        return file_path

    def save_data(self, file_path):
        usspass[f"try{self.count}"] = {"success": self.success, "ip": self.my_ip, "username": self.username, "password": self.password, "count": self.count, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        with open(file_path, "w") as file:
            json.dump(usspass, file, indent=4)

    def verify(self, file_path):
        if usspass[f"try{self.count}"]["username"] == self.my_username and usspass[f"try{self.count}"]["password"] == self.my_password:
            print("Login successful")
            self.success = True
            new_file_path = os.path.join(main_path, f"usspass_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json")
            self.save_data(new_file_path)
            usspass = {}
            with open(file_path, "w") as file:
                json.dump(usspass, file, indent=4)
            self.count = 1
        else:
            print("Login failed")
            self.count += 1
            self.main()
        self.count += 1

    def main(self):
        file_path = self.login()
        self.save_data(file_path)
        self.verify(file_path)


def run_user():
    user = User()
    user.main()


if __name__ == "__main__":
    run_user()
