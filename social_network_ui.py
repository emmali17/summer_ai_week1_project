# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2: Login")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. Send messages")
    print("5. View all my messages")
    print("6. <- Go back ")
    return input("Please Choose a number: ")


def editMyDetails():
    print("")
    print("1. Edit Name")
    print("2. Edit Age")
    print("3. Block Friends")
    return input("Please Choose a number: ")
