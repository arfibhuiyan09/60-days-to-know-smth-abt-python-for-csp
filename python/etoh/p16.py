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
    ],

    "steeple of wicked grotto": [
        "it is an Intense (Bottom) Difficulty steeple",
        "It was made by IroidIsABeast and blooby_jpg",
        "This steeple is a descending steeple",
        "This steeple is very forgiving, allowing the player to not lose much progress from falling",
        "This steeple is located in Silent Abyss."
    ],

    "citadel of laptop splitting": [
        "it is an Intense (Mid) Difficulty citadel",
        "It was made by Jukecalla",
        "This citadel had a gold star before the star system was discontinued",
        "This citadel was once Bottom Remorseless, but was moved down to Mid Intense due to it feeling easier",
        "This citadel is in Ring 1"
    ],

    "steeple of huge pain": [
        "it is an Intense (Low-Mid) Difficulty steeple",
        "It was made by AzaZeall",
        "This steeple's progression goes from F1, F2, F3, F5, F4",
        "This steeple is very loop-failable, however it has a safety net at Floor 5 and Floor 4",
        "This steeple is located in Forgotten Ridge."
    ],

    "citadel of a cruel tale": [
        "it is a Remorseless (High) Difficulty citadel",
        "It was made by aetrnalis",
        "This citadel was partially inspired by Citadel of Heights and Depths and Tower of Suffering Outside",
        "Floor 17 is supposedly 4 floors long, but due to outside sections it counts as only 1 floor",
        "This citadel is in Zone 7."
    ],

    "tower of astral fusion": [
        "it is a Remorseless (Bottom) Difficulty tower",
        "It was made by aethernetr",
        "This tower is a descending tower",
        "This tower is very forgiving, including a safety net on every single floor",
        "This tower is located in Zone 6."
    ],

    "maybe a tower": [
        "it is an Easy (Bottom) Mini Tower",
        "It was made by Obrentune",
        "This is the shortest Mini Tower in EToH",
        "This tower does not award a Tower Point but gives a badge called 'You Could Probably Call This a Tower'",
        "This Mini Tower is in Ring 2"
    ],

    "tower of fly high": [
        "it is a Hard (Low) Difficulty tower",
        "It was made by Zabregah and dreamyallyy",
        "This tower frame makes it unique by incorporating environments in each floor",
        "Two more environments were planned but scrapped due to time constraints",
        "This tower is in Steelspire Horizon."
    ],

    "tower of geometric kinetics": [
        "it is a Remorseless (Low-Mid) Difficulty tower",
        "It was made by DuskPyramid",
        "This tower had a unique frame unlike any other tower",
        "This tower's main gimmick is morphers used throughout",
        "This tower is in Steelspire Horizon."
    ],

    "tower of speeding right through": [
        "it is an Insane (Low-Mid) Difficulty tower",
        "It was made by VeryMuch_MC",
        "This tower takes inspiration from ToTUTU, ToCBTS, and ToSL",
        "This tower's main gimmick is speed boosters",
        "This tower is located in Steelspire Horizon."
    ],

    "tower of fatness": [
        "it is a Hard (Mid) Difficulty tower",
        "It was made by latomludo",
        "This tower is heavily disliked by the EToH community",
        "This tower is known for repetitive gameplay and a major spike in the last 3 floors",
        "This tower is located in Ring 3."
    ],

    "tower of complexity and volatility": [
        "it is a Terrifying (Bottom-Low) Difficulty tower",
        "It was made by Miantoz1980, znotfireman, ConfirmedIlluminatix",
        "This tower won 'Best Gameplay' in the 2025 EToH Awards",
        "This tower is well respected in the community and has stunning visuals",
        "This tower is in Zone 10."
    ]
}

def playquiz():
    print("\noka so i will give you 5 hints to what the tower is, if you can get it, you win! the hints get more specific the more you get wrong. (WRITE THE FULL NAME)")
    print("\n")
    s_tower = random.choice(list(towers.keys()))
    hints = towers[s_tower]
    count = 5
    print(f"you have {count} attempts left.")
    for i in range(5):
        print(hints[i])
        answer = input("Which tower is this: ").lower()
        if answer == s_tower:
            print(f"good job! the tower was {s_tower}!, you got it with {count} attempts left")
            print("\n")
            break
        else:
            print("no")
            count -= 1
            print(f"you have {count} attempts left")
        if count == 0:
            print(f"you have lost, the tower was {s_tower}.")
            print("\n")

while True:
    choice = input("do you want to play a guessing game that is themed around the ROBLOX game 'Eternal Towers of Hell'? (Y/N) ").lower().strip()
    if choice == "y":
        playquiz()
        choice2 = input("Do you want to play again? (Y/N) ").lower().strip()
        if choice2 == "y":
            playquiz()
        elif choice2 == "n":
            print("oka")
            break
        else:
            print(f"--> Error: '{choice2}' is an invalid prompt answer!")
    elif choice =="n":
        print("oh oka")
        break
    else:
        print(f"--> Error: '{choice}' is an invalid prompt answer!")
