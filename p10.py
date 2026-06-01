#number guessing game /// 05/31/26 /// Day 3

import random
count=1
attempts=7
guess=0
win=0
min, max = 1, 1000

while not win:
    choice = input("want to play number game (Y/N) ").lower().strip()
    if choice == "y":
        number = random.randint(min,max)
        while True:
            guess = int(input(f"oka guess a random number from a 1-1000. You have {attempts} attempts left "))
            if guess > number:
                print(f"{guess} is too high!")
                attempts -=1
                count +=1
            elif guess < number:
                print(f"{guess} is too low!")
                attempts -=1
                count +=1
            elif guess == number:
                print(f"GGs, the answer was {number}. you got the answer in {count}/7 total attempts!")
                win = True
                break
            if attempts == 0:
                print("You have ran out of attempts...")
                attempts = 7
                guess = 0
                break
            
    elif choice == "n":
        print("oka")
        break
    else:
        print(f"--> Error: '{choice}' is an invalid prompt answer!")
