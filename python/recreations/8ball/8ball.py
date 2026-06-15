import time
import random

word_bank = [
    "yes",
    "no",
    "maybe",
    "perhaps",
    "i dont think",
    "there might be a chance",
    "i think",
    "definitely",
    "absolutely",
    "probably",
    "unlikely",
    "not sure",
    "i guess so",
    "i doubt it",
    "most likely",
    "possibly",
    "could be",
    "i'm not certain",
    "i have no idea",
    "leaning yes",
    "leaning no",
    "hard to say",
    "it depends",
    "for sure",
    "no way",
    "sounds possible",
    "sounds unlikely"
]

def decision():
    choice = input("Ask a yes/no question: ")
    print(f"oka, you said {choice}. i need some time to think of an answer.")
    for i in range(3):
        print("thinking" + "." * (i + 1))
        time.sleep(1)
    selection = random.choice(word_bank)
    print(f"{selection}")

#initial run
decision()

while True:
    choice2 = input("do you have another sentence for me to make a decision on? (Y/N)").lower().strip()
    if choice2 == "y":
        decision()
    elif choice2 == "n":
        print("oka")
        break
    else:
        print(f"--> Error: '{choice2}' is an invalid prompt answer!")