import random
import time

month_map = {
"jan": "january",
"feb": "february",
"mar": "march",
"apr": "april",
"may": "may",
"jun": "june",
"jul": "july",
"aug": "august",
"sep": "september",
"oct": "october",
"nov": "november",
"dec": "december"
}

funfacts = {
"january": [
"January is named after Janus, the Roman god of beginnings and transitions.",
"January was not originally the first month of the Roman calendar.",
"January always has 31 days.",
"The Wolf Moon is the traditional full moon name for January.",
"New Year's Day is celebrated on January 1.",
"January is one of the coldest months in the Northern Hemisphere.",
"In the Southern Hemisphere, January is a summer month.",
"The birthstone for January is garnet.",
"The California Gold Rush began after a discovery in January 1848.",
"New Year’s resolutions date back over 4,000 years to ancient Babylon."
],

"february": [
"February is the shortest month of the year.",
"Leap Day occurs on February 29 during leap years.",
"February is named after the Roman festival Februa.",
"Valentine’s Day is celebrated on February 14.",
"Groundhog Day is celebrated on February 2 in the United States."
],

"march": [
"March is named after Mars, the Roman god of war.",
"March was originally the first month of the Roman calendar.",
"The spring equinox usually occurs in March.",
"St. Patrick’s Day is celebrated on March 17."
],

"april": [
"April Fool’s Day is celebrated on April 1.",
"Earth Day is celebrated on April 22.",
"April has 30 days.",
"Many trees begin growing new leaves in April."
],

"may": [
"May is named after Maia, a Roman goddess of growth.",
"Mother’s Day is celebrated in May in many countries.",
"Memorial Day is observed in the United States during May."
],

"june": [
"June is named after Juno, the Roman queen of the gods.",
"The summer solstice occurs in June in the Northern Hemisphere.",
"Many weddings take place in June."
],

"july": [
"July is named after Julius Caesar.",
"Independence Day in the United States is celebrated on July 4.",
"July has 31 days."
],

"august": [
"August is named after Augustus Caesar.",
"August has 31 days.",
"Many schools begin a new academic year in August."
],

"september": [
"September comes from the Latin word for seven.",
"The autumn equinox usually occurs in September.",
"Many students return to school in September."
],

"october": [
"October comes from the Latin word for eight.",
"Halloween is celebrated on October 31.",
"October is known for colorful autumn leaves."
],

"november": [
"November comes from the Latin word for nine.",
"Thanksgiving is celebrated in the United States in November.",
"Veterans Day is observed on November 11 in the United States."
],

"december": [
"December comes from the Latin word for ten.",
"Christmas is celebrated on December 25.",
"New Year’s Eve is celebrated on December 31."
]
}


# ---------------- FUNCTIONS ----------------

def countdown():
    print("oka, 5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)


def c(choice3):
    if choice3 == "y":
        print("oh wow thats cool ig")
    elif choice3 == "n":
        print("oh oka no worries lol")
        return False
    else:
        print("--> Error: '{}' is invalid".format(choice3))
        return False

    choice4 = input("do you want another fun fact? (Y/N) ").lower().strip()

    if choice4 == "y":
        return True
    elif choice4 == "n":
        print("oka")
        return False
    else:
        print("--> Error: '{}' is invalid".format(choice4))
        return False


def funfactsfunc(month):
    print("oka so you picked {}".format(month))

    while True:
        choice2 = input("see fun fact? (Y/N) ").lower().strip()

        if choice2 == "y":
            while True:
                fact = random.choice(funfacts[month])
                countdown()

                answer = input("did you know that {}? (Y/N) ".format(fact)).lower().strip()

                if not c(answer):
                    break

        elif choice2 == "n":
            print("oh oka")
            break

        else:
            print("--> Error: '{}' is invalid".format(choice2))


def runquiz(questions):
    random.shuffle(questions)

    print("quiz starting...\n")
    count = 0

    for i in range(len(questions)):
        prompt = questions[i][0]
        answer = questions[i][1]

        print("Q{}: {}".format(i+1, prompt))
        user = input("Your answer: ").lower()

        if user == answer:
            print("good job")
            count += 1
        else:
            print("no")

    percent = 100 * count / len(questions)
    percent = round(percent, 2)

    print("Score: {}/{} = {}%".format(count, len(questions), percent))


def easyquiz():
    questions = [
        ("January is named after Janus. Which month is this?", "january"),
        ("Valentine's Day happens in this month. Which month is this?", "february"),
        ("St. Patrick's Day is in this month. Which month is this?", "march")
    ]
    runquiz(questions)


def mediumquiz():
    questions = [
        ("Named after Janus, god of beginnings. Which month?", "january"),
        ("Leap Day occurs during this month. Which month?", "february"),
        ("Originally first Roman calendar month. Which month?", "march")
    ]
    runquiz(questions)


def hardquiz():
    questions = [
        ("Wolf Moon month. Which month?", "january"),
        ("Shortest month. Which month?", "february"),
        ("Summer solstice month. Which month?", "june")
    ]
    runquiz(questions)


def pqc():
    choice = input("go again? (Y/N) ").lower().strip()
    if choice == "y":
        print("oka")
    elif choice == "n":
        print("oka")
    else:
        print("--> Error: '{}' invalid".format(choice))


# ---------------- MAIN LOOP ----------------

while True:
    choice1 = input("fun facts or quiz? ").lower().strip()

    if choice1 == "fun facts":
        m = input("which month? ").lower().strip()

        if m in funfacts:
            funfactsfunc(m)
        elif m in month_map:
            funfactsfunc(month_map[m])
        else:
            print("--> Error: '{}' invalid".format(m))

    elif choice1 == "quiz":
        quiz = input("easy, medium, hard, quit? ").lower().strip()

        if quiz == "easy":
            easyquiz()
            pqc()
        elif quiz == "medium":
            mediumquiz()
            pqc()
        elif quiz == "hard":
            hardquiz()
            pqc()
        elif quiz == "quit":
            break
        else:
            print("--> Error: '{}' invalid".format(quiz))

    else:
        print("--> Error: '{}' invalid".format(choice1))
