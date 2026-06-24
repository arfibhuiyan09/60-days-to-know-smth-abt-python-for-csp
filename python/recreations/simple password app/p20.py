from time import sleep
import random

def createaccount():
    username = input("oka what would you like your username to be? ").strip()
    password = input(f"and what password would you like attached to '{username}'? ")

    print("oka, wait a few pls")
    time_duration = random.randint(1,4)
    sleep(time_duration)

    user_dict = {username: password}
    print(f"oka you have created your password with username {username} and password {password}!")
    return user_dict

def loginaccount(user_dict):
        a = True
        while a == True:
            login_attempt = input("oka, what is the username of the account you are trying to login into? ").strip()
            if login_attempt in user_dict:
                while a == True:
                    login_password = input(f"oka, what is your password? ")
                    if login_password == user_dict[login_attempt]:
                        print("Success: you have been logged in!")
                        a = False
                    else:
                        print("Error: the password you have typed in is wrong.")
                        choice2 = input("would you like to try again? (Y/N) ").lower().strip()
                        if choice2 == "y":
                            continue
                        elif choice2 == "n":
                            print("oka")
                            a = False
                        else:
                            print(f"--> Error: '{choice2}' is an invalid prompt answer!")
            else:
                print(f"--> Error: '{login_attempt}' was not found in our database!")
                choice2 = input("would you like to try again? (Y/N) ").lower().strip()
                if choice2 == "y":
                    continue
                elif choice2 == "n":
                    print("oka")
                    a = False
                else:
                    print(f"--> Error: '{choice2}' is an invalid prompt answer!")
while True:
    choice = input("hi! would you like to create an account, or login to an preexisting account? ('create' OR 'login' OR 'quit') ").lower().strip()
    if choice == "create":
        user_dict = createaccount()
    elif choice == "login":
        try:
            loginaccount(user_dict)
        except NameError:
            print("--> Error: you need to create an account to login to an account!")
            print("Try Again...\n")
    elif choice == "quit":
        print("oka")
        break
    else:
        print(f"--> Error: '{choice}' is an invalid prompt answer!")