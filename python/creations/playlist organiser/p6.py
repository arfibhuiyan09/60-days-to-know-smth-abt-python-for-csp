# Day 2 (05/30/26):
# playlist organiser using while loops and for loops
playlist = []

while True:
    choice = input("do you want to add, play, remove, or quit?  ").lower()
    if choice == "add":
        addition = input("what song do you want to add?  ")
        playlist.append(addition)
        print(f"your playlist now contains {len(playlist)} song(s) with {playlist}")
        
    elif choice == "play":
       print("now playing:")
       for i, song in enumerate(playlist):
        print(f"{i+1} - {song} ")
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