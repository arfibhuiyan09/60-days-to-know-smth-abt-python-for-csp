import sys

blacklist = ["admin",
            "0",
            "null",
            "administrator",
            "root",
            "sysadmin",
            "webmaster",
            "hostmaster",
            "manager",
            "support",
            "helpdesk",
            "www",
            "login",
            "logout",
            "register",
            "dashboard",
            "index",
            "api",
            "assets",
            "privacy",
            "contact",
            "staff",
            "team",
            "moderator",
            "mod",
            "official",
            "[WebsiteName]Support",
            "[WebsiteName]Admin",
            "user",
            "user1",
            "guest",
            "member",
            "anonymous",
            "info",
            "billing"
            ]
            

username = input("Enter a username to 'clean': ")
cleaned_username = username.lower().strip().replace(" ","_")
if cleaned_username == "":
    print("Username cannot be empty.")
    sys.exit()

def isfirstletteralphabet(cleaned_username):
    if not cleaned_username[0].isalpha():
        print(f"Your username must start with a letter. not {cleaned_username[0]}.")
        sys.exit()
    
def reserved_user(cleaned_username):
    if cleaned_username in blacklist:
        print(f"You can not have the username {cleaned_username}.")
        sys.exit()

if 3 <= len(cleaned_username) <= 64:
    reserved_user(cleaned_username)
    isfirstletteralphabet(cleaned_username)
    print(f"your cleaned username is {cleaned_username}!")
else:
    print(f"your username's char ct MUST be between 3-64 char, not {len(username)} char.")