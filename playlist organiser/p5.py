# Day 2 (05/30/26):
# playlist organiser using while loops
playlist = []

while True:
    choice = input("do you want to add, play, remove, or quit?  ").lower()
    if choice == "add":
        addition = input("what song do you want to add?  ")
        playlist.append(addition)
        print(f"your playlist now contains {len(playlist)} song(s) with {playlist}")
        
    elif choice == "play":
        question = input("would you like to play the whole playlist ? (Y/N)").lower()
        if question == "y":
            print(f"playing {playlist}!")
        elif question == "n":
            question2 = input("would you like to play the latest song then? (Y/N)").lower()
            if question2 == "y":
                print(f"playing {playlist[-1]}!")
            elif question2 == "n":
                print("ogh")
            else:
                print(f"--> Error: '{question2}' is an invalid prompt answer!")
        else:
            print(f"--> Error: '{question}' is an invalid prompt answer!")
    elif choice == "remove":
        removal = input("what song do you want to remove?  ")
        if removal in playlist:
            playlist.remove(removal)
            print(f"your playlist now contains {len(playlist)} song(s) with {playlist}")
        else:
            print(f"Error: there was no instance of {removal} in the playlist!")
    elif choice == "quit":
        print("oka!")
        break 
    else:
        print(f"--> Error: '{choice}' is an invalid prompt answer!")