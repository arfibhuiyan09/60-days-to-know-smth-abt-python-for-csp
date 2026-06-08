import random

count = 1
attempts = 7
guess = 0
win = False
min_val = 1
max_val = 1000

while not win:

    choice = input("want to play number game (Y/N) ").lower().strip()

    if choice == "y":

        number = random.randint(min_val, max_val)

        while True:

            guess = int(input("guess a number 1-1000. attempts left: {} ".format(attempts)))

            if guess > number:
                print("{} is too high!".format(guess))
                attempts -= 1
                count += 1

            elif guess < number:
                print("{} is too low!".format(guess))
                attempts -= 1
                count += 1

            elif guess == number:
                print("GGs, the answer was {}. you got it in {}/7 attempts!".format(number, count))
                win = True
                break

            if attempts == 0:
                print("You have run out of attempts...")
                break

    elif choice == "n":
        print("oka")
        break

    else:
        print("--> Error: '{}' is an invalid prompt answer!".format(choice))
