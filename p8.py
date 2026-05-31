import random
def fighter_initialization():
    name1 = input("Enter the name of your first fighter:  ")
    attack1a = input("Describe what ability your first figher shall have:  ")
    attack1b = input("Describe what sub-ability your first figher shall have:  ")
    name2 = input("Enter the name of your second fighter:  ")
    attack2a = input("Describe what ability your second figher shall have:  ")
    attack2b = input("Describe what sub-ability your second figher shall have:  ")
    print(f"for confirmation, Fighter 1 is {name1}, whom has a ability of {attack1a} and a subability of {attack1b}, and Fighter 2 is {name2}, whom has an ability of {attack2a} and a subability of {attack2b}  ")
    print("KEY: the ability does 10-25HP per move while the subability does 1-40HP per move.")

    return {
        "name1": name1, "attack1a": attack1a, "attack1b": attack1b,
        "name2": name2, "attack2a": attack2a, "attack2b": attack2b
    }

def battle(fighters):
    #default health
    # also health 1 = player 2, health 2 = player 1. very counterintuative i know. 
    health1 = 100
    health2 = 100
    #show default health
    print(f"{fighters['name1']} has {health1} HP,")
    print(f"{fighters['name2']} has {health2} HP,")
    while True:
        #define damage1a, damage 1b, damage 2a, damage 2b
        damage1a = 0
        damage1b = 0
        damage2a = 0
        damage2b = 0

        #ask fighter 1 for input
        selection1 = input(f"it is {fighters['name1']}'s turn, which ability would you like to pick? ({fighters['attack1a']}, or {fighters['attack1b']})  ")
        if selection1 == fighters['attack1a']:
          #calculates damage by choosing a random number
          damage1a = random.randint(10,25)
          print(f"{fighters['name1']} has attacked {fighters['name2']} with {fighters['attack1a']} and did {damage1a} dmg!")
          #if player 1 attacks using attack1a
          updated_health1a = health1-damage1a
          #prints how much health player 2 has
          print(f"{fighters['name2']} has {updated_health1a} HP")
          health1=updated_health1a
        elif selection1 == fighters['attack1b']:
            #calculates damage by choosing a random number
            damage1b = random.randint(1,40)
            print(f"{fighters['name1']} has attacked {fighters['name2']} with {fighters['attack1b']} and did {damage1b} dmg!")
            #if player 1 attacks using attack1b
            updated_health1b = health1-damage1b
            #prints how much health player 2 has
            print(f"{fighters['name2']} has {updated_health1b} HP")
            health1=updated_health1b
        else:
            print(f"--> Error: '{selection1}' is an invalid prompt answer!")

         #check if the health for both players have depleted fully
        if health1 <= 0:
            print(f"GGs, {fighters['name1']} wins! with {health2} HP remaining!")
            break
        else:
            pass
        if health2 <=0:
            print(f"GGs, {fighters['name2']} wins! with {health2} HP remaining!")
            break
        else:
            pass
        
        #ask fighter 2 for input
        selection2 = input(f"it is {fighters['name2']}'s turn, which ability would you like to pick? ({fighters['attack2a']}, or {fighters['attack2b']})   ")
        if selection2 == fighters['attack2a']:
          #calculates damage by choosing a random number
          damage2a = random.randint(10,25)
          print(f"{fighters['name2']} has attacked {fighters['name1']} with {fighters['attack2a']} and did {damage2a} dmg!")
          #if player 2 attacks using attack2a
          updated_health2a = health2-damage2a
          #prints how much health player 1 has
          print(f"{fighters['name1']} has {updated_health2a} HP")
          health2=updated_health2a
        elif selection2 == fighters['attack2b']:
            #calculates damage by choosing a random number
            damage2b = random.randint(1,40)
            print(f"{fighters['name2']} has attacked {fighters['name1']} with {fighters['attack2b']} and did {damage2b} dmg!")
            #if player 2 attacks using attack2b
            updated_health2b = health2-damage2b
            #prints how much health player 1 has
            print(f"{fighters['name1']} has {updated_health2b} HP")
            health2=updated_health2b
        else:
            print(f"--> Error: '{selection2}' is an invalid prompt answer!")

        #check if the health for both players have depleted fully
        if health1 <= 0:
            print(f"GGs, {fighters['name1']} wins! with {health2} HP remaining!")
            break
        else:
            pass
        if health2 <=0:
            print(f"GGs, {fighters['name2']} wins! with {health1} HP remaining!")
            break
        else:
            pass
        


choice = input("welcome to the 2 player fighting game, this game requires consent so do you want to play? (Y/N)"  ).lower()
if choice == "y":
    fighters = fighter_initialization()
    fight_start = input("would you like to start the fight? (Y/N)  ").lower()
    if fight_start == "y":
        battle(fighters)
    elif fight_start == "n":
        print("oh ok")
    else:
        print(f"--> Error: '{fight_start}' is an invalid prompt answer!")
    
elif choice == "n":
    print("oka")
else:
    print(f"--> Error: '{choice}' is an invalid prompt answer!")