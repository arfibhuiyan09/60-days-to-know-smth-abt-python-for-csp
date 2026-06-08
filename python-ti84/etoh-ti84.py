import random

towers = {
"tower of versatility": [
"it is a Difficult (Mid-High) Difficulty tower",
"It was made by Auterus",
"This tower replaced ToOEZ",
"This tower was Hard difficulty originally before getting into its area",
"This tower is located in Forgotten Ridge."
],

"tower of hecc": [
"it is a Hard (Low) Difficulty tower",
"It was made by Obrentune",
"This tower helped inspire the creation of Tower of Hell",
"This tower existed during the KToH era of EToH",
"This Tower is in Ring 1"
],

"tower of watts": [
"it is an Intense (Low-Mid) Difficulty tower",
"It was made by Devin_Darksword and RageFurious",
"This tower was originally Hard difficulty but then moved up to Challenging, and finally Intense",
"This tower has a gradient going from light blue to dark blue",
"This tower is located in Zone 6."
],

"tower of astral eclipse": [
"it is an Extreme (Base) Difficulty tower",
"It was made by Cll0y, Zabregah, and T3mpl4te",
"This tower has a final stretch",
"This tower had a monthly challenge turning this tower into a Citadel",
"This Tower is in Zone 8."
]
}

def playquiz():
    print("\noka so i will give you 5 hints to what the tower is")
    print("WRITE THE FULL NAME\n")

    s_tower = random.choice(list(towers))
    hints = towers[s_tower]

    count = 5
    print("you have {} attempts left.".format(count))

    for i in range(5):
        print(hints[i])
        answer = input("Which tower is this: ").lower()

        if answer == s_tower:
            print("good job! the tower was {}, you got it with {} attempts left".format(s_tower, count))
            print("\n")
            break
        else:
            print("no")
            count -= 1
            print("you have {} attempts left".format(count))

        if count == 0:
            print("you have lost, the tower was {}.".format(s_tower))
            print("\n")
            break


while True:
    choice = input("Do you want to play the ROBLOX EToH quiz? (Y/N) ").lower().strip()

    if choice == "y":
        playquiz()

        choice2 = input("Do you want to play again? (Y/N) ").lower().strip()

        if choice2 == "y":
            playquiz()
        elif choice2 == "n":
            print("oka")
            break
        else:
            print("--> Error: '{}' is an invalid prompt answer!".format(choice2))

    elif choice == "n":
        print("oh oka")
        break

    else:
        print("--> Error: '{}' is an invalid prompt answer!".format(choice))
