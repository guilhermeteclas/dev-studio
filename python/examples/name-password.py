name = input("Enter name: ")
password = input("Enter password: ")

while name == password:
    print("Name and password cannot be the same")
    name = input("Enter name: ")
    password = input("Enter password: ")