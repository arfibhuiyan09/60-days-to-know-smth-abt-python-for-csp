import random
import time

january_list = ["january", "jan"]
february_list = ["february", "feb"]
march_list = ["march", "mar"]
april_list = ["april", "apr"]
june_list = ["june", "jun"]
july_list = ["july", "jul"]
august_list = ["august", "aug"]
september_list = ["september", "sep"]
october_list = ["october", "oct"]
november_list = ["november", "nov"]
decemeber_list = ["december", "dec"]

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
        "February can pass without a full moon in some years.",
        "Groundhog Day is celebrated on February 2 in the United States.",
        "The birthstone for February is amethyst.",
        "The birth flower for February is the violet.",
        "February is part of meteorological winter in the Northern Hemisphere.",
        "The zodiac signs for February are Aquarius and Pisces."
    ],
    "march": [
        "March is named after Mars, the Roman god of war.",
        "March was originally the first month of the Roman calendar.",
        "The spring equinox usually occurs in March.",
        "St. Patrick’s Day is celebrated on March 17.",
        "March Madness is a major U.S. college basketball tournament.",
        "March often marks the beginning of spring.",
        "The birthstone for March is aquamarine.",
        "The birth flower for March is the daffodil.",
        "March and November often begin on the same weekday in non-leap years.",
        "The name March comes from the Latin month Martius."
    ],
    "april": [
        "April is thought to come from the Latin word 'aperire,' meaning to open.",
        "April Fool’s Day is celebrated on April 1.",
        "Earth Day is celebrated on April 22.",
        "April has 30 days.",
        "The birthstone for April is diamond.",
        "The birth flower for April is the daisy.",
        "Many trees begin growing new leaves in April.",
        "April is associated with spring rain and flowers.",
        "April always ends on the same weekday as December.",
        "The zodiac signs for April are Aries and Taurus."
    ],
    "may": [
        "May is named after Maia, a Roman goddess of growth.",
        "May has 31 days.",
        "Mother’s Day is celebrated in May in many countries.",
        "Memorial Day is observed in the United States during May.",
        "May is associated with spring flowers and warmer weather.",
        "Many schools hold graduations in May.",
        "The birthstone for May is emerald.",
        "The birth flower for May is the lily of the valley.",
        "May is one of only three months that never starts on the same weekday as another month.",
        "The zodiac signs for May are Taurus and Gemini."
    ],
    "june": [
        "June is named after Juno, the Roman queen of the gods.",
        "June has 30 days.",
        "The summer solstice occurs in June in the Northern Hemisphere.",
        "June has the longest daylight hours of the year in the Northern Hemisphere.",
        "Many weddings take place in June.",
        "Father’s Day was first celebrated in June 1910.",
        "The birthstone for June is pearl.",
        "The birth flower for June is the rose.",
        "June marks the beginning of summer in the Northern Hemisphere.",
        "June is associated with Pride Month celebrations."
    ],
    "july": [
        "July is named after Julius Caesar.",
        "July was originally called Quintilis in the Roman calendar.",
        "Independence Day in the United States is celebrated on July 4.",
        "July has 31 days.",
        "The first moon landing occurred on July 20, 1969.",
        "July is typically one of the hottest months in the Northern Hemisphere.",
        "The birthstone for July is ruby.",
        "The birth flower for July is the larkspur.",
        "July and January begin on the same weekday in non-leap years.",
        "The zodiac signs for July are Cancer and Leo."
    ],
    "august": [
        "August is named after Augustus Caesar.",
        "August has 31 days.",
        "Many schools begin a new academic year in August.",
        "The Perseid meteor shower peaks in August.",
        "August is often one of the hottest months of the year.",
        "August was originally called Sextilis in the Roman calendar.",
        "The birthstone for August is peridot.",
        "The birth flower for August is the gladiolus.",
        "August and February begin on the same weekday in leap years.",
        "The zodiac signs for August are Leo and Virgo."
    ],
    "september": [
        "September comes from the Latin word for seven.",
        "September has 30 days.",
        "The autumn equinox usually occurs in September.",
        "September marks the beginning of autumn in the Northern Hemisphere.",
        "Many students return to school in September.",
        "The birthstone for September is sapphire.",
        "The birth flower for September is the aster.",
        "September was originally the seventh month of the Roman calendar.",
        "The zodiac signs for September are Virgo and Libra.",
        "September is a common month for birthdays."
    ],
    "october": [
        "October comes from the Latin word for eight.",
        "October has 31 days.",
        "Halloween is celebrated on October 31.",
        "October is known for colorful autumn leaves.",
        "Many harvest festivals occur in October.",
        "The birthstone for October is opal.",
        "The birth flower for October is the marigold.",
        "October was originally the eighth month of the Roman calendar.",
        "October and January often begin on the same weekday.",
        "The zodiac signs for October are Libra and Scorpio."
    ],
    "november": [
        "November comes from the Latin word for nine.",
        "November has 30 days.",
        "Thanksgiving is celebrated in the United States in November.",
        "Veterans Day is observed on November 11 in the United States.",
        "November is associated with falling leaves and colder weather.",
        "The birthstone for November is topaz.",
        "The birth flower for November is the chrysanthemum.",
        "November was originally the ninth month of the Roman calendar.",
        "November and March often begin on the same weekday.",
        "The zodiac signs for November are Scorpio and Sagittarius."
    ],
    "december": [
        "December comes from the Latin word for ten.",
        "December has 31 days.",
        "Christmas is celebrated on December 25.",
        "New Year’s Eve is celebrated on December 31.",
        "The winter solstice occurs in December in the Northern Hemisphere.",
        "December is associated with many global holidays.",
        "The birthstone for December is turquoise.",
        "The birth flower for December is the narcissus.",
        "December was originally the tenth month of the Roman calendar.",
        "The zodiac signs for December are Sagittarius and Capricorn."
    ]
}

# month functions
def january():
    print("oka so you are either a Capricorn or Aquarius.")
    while True:
        choice2 = input("oka so would you like to see your fun fact? (Y/N) ").lower().strip()
        if choice2 == "y":
            while True:
                randomjan_fact = random.choice(funfacts["january"])
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
                choice3 = input(f"did you know that {randomjan_fact}? (Y/N) ").lower().strip()
                if choice3 == "y":
                    print("oh wow thats cool ig")
                elif choice3 == "n":
                    print("oh oka no worries lol")
                else:
                    print(f"--> Error: '{choice3}' is an invalid prompt answer!")
                choice4 = input("do you want a another funfact about January? (Y/N) ").lower().strip()
                if choice4 == "y":
                    pass
                elif choice4 == "n":
                    print("oka")
                    break
                else:
                    print(f"--> Error: '{choice4}' is an invalid prompt answer!")

        elif choice2 == "n":
            print("oh oka")
            break
        else:
            print(f"--> Error: '{choice2}' is an invalid prompt answer!")
def february():
    print("oka so you are either a Aquarius or Pisces.")
    while True:
        choice2 = input("oka so would you like to see your fun fact? (Y/N) ").lower().strip()
        if choice2 == "y":
            while True:
                randomfeb_fact = random.choice(funfacts["february"])
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
                choice3 = input(f"did you know that {randomfeb_fact}? (Y/N) ").lower().strip()
                if choice3 == "y":
                    print("oh wow thats cool ig")
                elif choice3 == "n":
                    print("oh oka no worries lol")
                else:
                    print(f"--> Error: '{choice3}' is an invalid prompt answer!")
                choice4 = input("do you want a another funfact about February? (Y/N) ").lower().strip()
                if choice4 == "y":
                    pass
                elif choice4 == "n":
                    print("oka")
                    break
                else:
                    print(f"--> Error: '{choice4}' is an invalid prompt answer!")

        elif choice2 == "n":
            print("oh oka")
            break
        else:
            print(f"--> Error: '{choice2}' is an invalid prompt answer!")
def march():
    print("oka so you are either a Pisces or Aries.")
    while True:
        choice2 = input("oka so would you like to see your fun fact? (Y/N) ").lower().strip()
        if choice2 == "y":
            while True:
                randommar_fact = random.choice(funfacts["march"])
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
                choice3 = input(f"did you know that {randommar_fact}? (Y/N) ").lower().strip()
                if choice3 == "y":
                    print("oh wow thats cool ig")
                elif choice3 == "n":
                    print("oh oka no worries lol")
                else:
                    print(f"--> Error: '{choice3}' is an invalid prompt answer!")
                choice4 = input("do you want a another funfact about March? (Y/N) ").lower().strip()
                if choice4 == "y":
                    pass
                elif choice4 == "n":
                    print("oka")
                    break
                else:
                    print(f"--> Error: '{choice4}' is an invalid prompt answer!")

        elif choice2 == "n":
            print("oh oka")
            break
        else:
            print(f"--> Error: '{choice2}' is an invalid prompt answer!")
def april():
    print("oka so you are either a Aries or Taurus.")
    while True:
        choice2 = input("oka so would you like to see your fun fact? (Y/N) ").lower().strip()
        if choice2 == "y":
            while True:
                randomapr_fact = random.choice(funfacts["april"])
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
                choice3 = input(f"did you know that {randomapr_fact}? (Y/N) ").lower().strip()
                if choice3 == "y":
                    print("oh wow thats cool ig")
                elif choice3 == "n":
                    print("oh oka no worries lol")
                else:
                    print(f"--> Error: '{choice3}' is an invalid prompt answer!")
                choice4 = input("do you want a another funfact about April? (Y/N) ").lower().strip()
                if choice4 == "y":
                    pass
                elif choice4 == "n":
                    print("oka")
                    break
                else:
                    print(f"--> Error: '{choice4}' is an invalid prompt answer!")

        elif choice2 == "n":
            print("oh oka")
            break
        else:
            print(f"--> Error: '{choice2}' is an invalid prompt answer!")
def may():
    print("oka so you are either a Taurus or Gemini.")
    while True:
        choice2 = input("oka so would you like to see your fun fact? (Y/N) ").lower().strip()
        if choice2 == "y":
            while True:
                randommay_fact = random.choice(funfacts["may"])
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
                choice3 = input(f"did you know that {randommay_fact}? (Y/N) ").lower().strip()
                if choice3 == "y":
                    print("oh wow thats cool ig")
                elif choice3 == "n":
                    print("oh oka no worries lol")
                else:
                    print(f"--> Error: '{choice3}' is an invalid prompt answer!")
                choice4 = input("do you want a another funfact about May? (Y/N) ").lower().strip()
                if choice4 == "y":
                    pass
                elif choice4 == "n":
                    print("oka")
                    break
                else:
                    print(f"--> Error: '{choice4}' is an invalid prompt answer!")

        elif choice2 == "n":
            print("oh oka")
            break
        else:
            print(f"--> Error: '{choice2}' is an invalid prompt answer!")
def june():
    print("oka so you are either a Gemini or Cancer.")
    while True:
        choice2 = input("oka so would you like to see your fun fact? (Y/N) ").lower().strip()
        if choice2 == "y":
            while True:
                randomjun_fact = random.choice(funfacts["june"])
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
                choice3 = input(f"did you know that {randomjun_fact}? (Y/N) ").lower().strip()
                if choice3 == "y":
                    print("oh wow thats cool ig")
                elif choice3 == "n":
                    print("oh oka no worries lol")
                else:
                    print(f"--> Error: '{choice3}' is an invalid prompt answer!")
                choice4 = input("do you want a another funfact about June? (Y/N) ").lower().strip()
                if choice4 == "y":
                    pass
                elif choice4 == "n":
                    print("oka")
                    break
                else:
                    print(f"--> Error: '{choice4}' is an invalid prompt answer!")

        elif choice2 == "n":
            print("oh oka")
            break
        else:
            print(f"--> Error: '{choice2}' is an invalid prompt answer!")
def july():
    print("oka so you are either a Cancer or Leo.")
    while True:
        choice2 = input("oka so would you like to see your fun fact? (Y/N) ").lower().strip()
        if choice2 == "y":
            while True:
                randomjul_fact = random.choice(funfacts["july"])
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
                choice3 = input(f"did you know that {randomjul_fact}? (Y/N) ").lower().strip()
                if choice3 == "y":
                    print("oh wow thats cool ig")
                elif choice3 == "n":
                    print("oh oka no worries lol")
                else:
                    print(f"--> Error: '{choice3}' is an invalid prompt answer!")
                choice4 = input("do you want a another funfact about July? (Y/N) ").lower().strip()
                if choice4 == "y":
                    pass
                elif choice4 == "n":
                    print("oka")
                    break
                else:
                    print(f"--> Error: '{choice4}' is an invalid prompt answer!")

        elif choice2 == "n":
            print("oh oka")
            break
        else:
            print(f"--> Error: '{choice2}' is an invalid prompt answer!")
def august():
    print("oka so you are either a Leo or Virgo.")
    while True:
        choice2 = input("oka so would you like to see your fun fact? (Y/N) ").lower().strip()
        if choice2 == "y":
            while True:
                randomaug_fact = random.choice(funfacts["august"])
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
                choice3 = input(f"did you know that {randomaug_fact}? (Y/N) ").lower().strip()
                if choice3 == "y":
                    print("oh wow thats cool ig")
                elif choice3 == "n":
                    print("oh oka no worries lol")
                else:
                    print(f"--> Error: '{choice3}' is an invalid prompt answer!")
                choice4 = input("do you want a another funfact about August? (Y/N) ").lower().strip()
                if choice4 == "y":
                    pass
                elif choice4 == "n":
                    print("oka")
                    break
                else:
                    print(f"--> Error: '{choice4}' is an invalid prompt answer!")

        elif choice2 == "n":
            print("oh oka")
            break
        else:
            print(f"--> Error: '{choice2}' is an invalid prompt answer!")
def september():
    print("oka so you are either a Virgo or Libra.")
    while True:
        choice2 = input("oka so would you like to see your fun fact? (Y/N) ").lower().strip()
        if choice2 == "y":
            while True:
                randomsep_fact = random.choice(funfacts["september"])
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
                choice3 = input(f"did you know that {randomsep_fact}? (Y/N) ").lower().strip()
                if choice3 == "y":
                    print("oh wow thats cool ig")
                elif choice3 == "n":
                    print("oh oka no worries lol")
                else:
                    print(f"--> Error: '{choice3}' is an invalid prompt answer!")
                choice4 = input("do you want a another funfact about September? (Y/N) ").lower().strip()
                if choice4 == "y":
                    pass
                elif choice4 == "n":
                    print("oka")
                    break
                else:
                    print(f"--> Error: '{choice4}' is an invalid prompt answer!")

        elif choice2 == "n":
            print("oh oka")
            break
        else:
            print(f"--> Error: '{choice2}' is an invalid prompt answer!")
def october():
    print("oka so you are either a Libra or Scorpio.")
    while True:
        choice2 = input("oka so would you like to see your fun fact? (Y/N) ").lower().strip()
        if choice2 == "y":
            while True:
                randomoct_fact = random.choice(funfacts["october"])
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
                choice3 = input(f"did you know that {randomoct_fact}? (Y/N) ").lower().strip()
                if choice3 == "y":
                    print("oh wow thats cool ig")
                elif choice3 == "n":
                    print("oh oka no worries lol")
                else:
                    print(f"--> Error: '{choice3}' is an invalid prompt answer!")
                choice4 = input("do you want a another funfact about October? (Y/N) ").lower().strip()
                if choice4 == "y":
                    pass
                elif choice4 == "n":
                    print("oka")
                    break
                else:
                    print(f"--> Error: '{choice4}' is an invalid prompt answer!")

        elif choice2 == "n":
            print("oh oka")
            break
        else:
            print(f"--> Error: '{choice2}' is an invalid prompt answer!")
def november():
    print("oka so you are either a Scorpio or Sagittarius.")
    while True:
        choice2 = input("oka so would you like to see your fun fact? (Y/N) ").lower().strip()
        if choice2 == "y":
            while True:
                randomnov_fact = random.choice(funfacts["november"])
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
                choice3 = input(f"did you know that {randomnov_fact}? (Y/N) ").lower().strip()
                if choice3 == "y":
                    print("oh wow thats cool ig")
                elif choice3 == "n":
                    print("oh oka no worries lol")
                else:
                    print(f"--> Error: '{choice3}' is an invalid prompt answer!")
                choice4 = input("do you want a another funfact about November? (Y/N) ").lower().strip()
                if choice4 == "y":
                    pass
                elif choice4 == "n":
                    print("oka")
                    break
                else:
                    print(f"--> Error: '{choice4}' is an invalid prompt answer!")

        elif choice2 == "n":
            print("oh oka")
            break
        else:
            print(f"--> Error: '{choice2}' is an invalid prompt answer!")
def december():
    print("oka so you are either a Sagittarius or Capricorn.")
    while True:
        choice2 = input("oka so would you like to see your fun fact? (Y/N) ").lower().strip()
        if choice2 == "y":
            while True:
                randomdec_fact = random.choice(funfacts["december"])
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
                choice3 = input(f"did you know that {randomdec_fact}? (Y/N) ").lower().strip()
                if choice3 == "y":
                    print("oh wow thats cool ig")
                elif choice3 == "n":
                    print("oh oka no worries lol")
                else:
                    print(f"--> Error: '{choice3}' is an invalid prompt answer!")
                choice4 = input("do you want a another funfact about December? (Y/N) ").lower().strip()
                if choice4 == "y":
                    pass
                elif choice4 == "n":
                    print("oka")
                    break
                else:
                    print(f"--> Error: '{choice4}' is an invalid prompt answer!")

        elif choice2 == "n":
            print("oh oka")
            break
        else:
            print(f"--> Error: '{choice2}' is an invalid prompt answer!") 

# quiz functions
def easyquiz():

    questions = [
                    ("January is named after Janus. Which month is this?", "january"),
                    ("Valentine's Day happens in this month. Which month is this?", "february"),
                    ("St. Patrick's Day is in this month. Which month is this?", "march"),
                    ("Earth Day is celebrated in this month. Which month is this?", "april"),
                    ("Mother's Day is often in this month. Which month is this?", "may"),
                    ("Father's Day starts summer celebrations in this month. Which month is this?", "june"),
                    ("Independence Day (USA) is in this month. Which month is this?", "july"),
                    ("Many schools start in this month. Which month is this?", "august"),
                    ("Autumn begins in this month. Which month is this?", "september"),
                    ("Halloween is in this month. Which month is this?", "october"),
                    ("Thanksgiving is in this month. Which month is this?", "november"),
                    ("Christmas is in this month. Which month is this?", "december")
                ]
    random.shuffle(questions)
    
    print(f"oka here is a quiz with 10 questions with a score evaluation at the end!\n")
    count = 0
    for index, (prompt,answer) in enumerate(questions):
        print(f"Q{index+1}: {prompt}")
        user_answer = input("Your answer: ").lower()
        if user_answer == answer:
            print("good job")
            count += 1
        else:
            print("no")
    percentage = 100*(count/len(questions))
    rounded_percentage = round(percentage, 2)
    def gradecalculation():
        if rounded_percentage > 90:
            return("A")
        elif rounded_percentage >= 80:
            return("B")
        elif rounded_percentage >= 70:
            return("C")
        elif rounded_percentage >= 60:
            return(" D")
        else: 
            return("F")
    print(f"you have gotten {count}/{len(questions)} correct, which is a {rounded_percentage}% ({gradecalculation()})")
def mediumquiz():
    medium_questions = [
    ("Named after Janus, the Roman god of beginnings and transitions. Which month is this?", "january"),
    ("Leap Day occurs during this month every four years. Which month is this?", "february"),
    ("Originally the first month of the Roman calendar. Which month is this?", "march"),
    ("Earth Day is celebrated in this month. Which month is this?", "april"),
    ("Named after Maia, a Roman goddess of growth. Which month is this?", "may"),
    ("Named after Juno, queen of the Roman gods. Which month is this?", "june"),
    ("Named after Julius Caesar. Which month is this?", "july"),
    ("Named after Augustus Caesar. Which month is this?", "august"),
    ("Comes from the Latin word for seven. Which month is this?", "september"),
    ("Comes from the Latin word for eight. Which month is this?", "october"),
    ("Comes from the Latin word for nine. Which month is this?", "november"),
    ("Comes from the Latin word for ten. Which month is this?", "december"),
    ("Has 28 or 29 days depending on leap years. Which month is this?", "february"),
    ("Often marks the beginning of spring in the Northern Hemisphere. Which month is this?", "march"),
    ("Often marks the beginning of autumn in the Northern Hemisphere. Which month is this?", "september") 
    ]
    random.shuffle(medium_questions)
    
    print(f"oka here is a quiz with 10 questions with a score evaluation at the end!\n")
    count = 0
    for index, (prompt,answer) in enumerate(medium_questions):
        print(f"Q{index+1}: {prompt}")
        user_answer = input("Your answer: ").lower()
        if user_answer == answer:
            print("good job")
            count += 1
        else:
            print("no")
    percentage = 100*(count/len(medium_questions))
    rounded_percentage = round(percentage, 2)
    def gradecalculation():
        if rounded_percentage > 90:
            return("A")
        elif rounded_percentage >= 80:
            return("B")
        elif rounded_percentage >= 70:
            return("C")
        elif rounded_percentage >= 60:
            return(" D")
        else: 
            return("F")
    print(f"you have gotten {count}/{len(medium_questions)} correct, which is a {rounded_percentage}% ({gradecalculation()})!")
def hardquiz():
    hard_questions = [
    ("Was originally not the first month in the Roman calendar and was added later. Which month is this?", "january"),
    ("Can pass without a full moon in some years. Which month is this?", "february"),
    ("Often begins on the same weekday as November in non-leap years. Which month is this?", "march"),
    ("Always ends on the same weekday as December. Which month is this?", "april"),
    ("One of only three months that never starts on the same weekday as another month. Which month is this?", "may"),
    ("Has the longest daylight hours in the Northern Hemisphere. Which month is this?", "june"),
    ("Often begins on the same weekday as January in non-leap years. Which month is this?", "july"),
    ("Begins on the same weekday as February in leap years. Which month is this?", "august"),
    ("Was originally the seventh month of the Roman calendar. Which month is this?", "september"),
    ("Was originally the eighth month of the Roman calendar. Which month is this?", "october"),
    ("Was originally the ninth month of the Roman calendar. Which month is this?", "november"),
    ("Was originally the tenth month of the Roman calendar. Which month is this?", "december"),
    ("Associated with the Perseid meteor shower peak. Which month is this?", "august"),
    ("Associated with the Wolf Moon in traditional naming. Which month is this?", "january"),
    ("Associated with the summer solstice in the Northern Hemisphere. Which month is this?", "june")
]
    random.shuffle(hard_questions)
    
    print(f"oka here is a quiz with 10 questions with a score evaluation at the end!\n")
    count = 0
    for index, (prompt,answer) in enumerate(hard_questions):
        print(f"Q{index+1}: {prompt}")
        user_answer = input("Your answer: ").lower()
        if user_answer == answer:
            print("good job")
            count += 1
        else:
            print("no")
    percentage = 100*(count/len(hard_questions))
    rounded_percentage = round(percentage, 2)
    def gradecalculation():
        if rounded_percentage > 90:
            return("A")
        elif rounded_percentage >= 80:
            return("B")
        elif rounded_percentage >= 70:
            return("C")
        elif rounded_percentage >= 60:
            return(" D")
        else: 
            return("F")
    print(f"you have gotten {count}/{len(hard_questions)} correct, which is a {rounded_percentage}% ({gradecalculation()})!")

# misc
def linebreak():
    print("\n")


#main code
while True:
    choice1 = input("hello! do you want to learn different facts about different months in the year or take a quiz of knowing facts from said month? ('fun facts' or 'quiz') ").lower().strip()
    if choice1 == "fun facts":
        choice1 = input("oka, which month are you? ").lower().strip()
        if choice1 in january_list:
            january()
        elif choice1 in february_list:
            february()
        elif choice1 in march_list:
            march()
        elif choice1 in april_list:
            april()
        elif choice1 == "may":
            may()
        elif choice1 in june_list:
            june()
        elif choice1 in july_list:
            july()
        elif choice1 in august_list:
            august()
        elif choice1 in september_list:
            september()
        elif choice1 in october_list:
            october()
        elif choice1 in november_list:
            november()
        elif choice1 in decemeber_list:
            december()
        else:
            print(f"--> Error: '{choice1}' is an invalid prompt answer!")
    elif choice1 == "quiz":
        while True:
            quiz_choice = input("ok, do you want to do a Easy, Medium, or Hard quiz about the fun facts about each month or do you want to quit? ('easy', 'medium', 'hard' 'quit') ").lower().strip()
            if quiz_choice == "easy":
                while True:
                    easyquiz()
                    pqc = input("do you want to go again? (Y/N) ").lower().strip()
                    if pqc == "y":
                        print("oka")
                        linebreak()
                    elif pqc == "n":
                        print("oka")
                        linebreak()
                        break
                    else:
                        print(f"--> Error: '{pqc}' is an invalid prompt answer!")
            elif quiz_choice == "medium":
                while True:
                    mediumquiz()
                    pqc = input("do you want to go again? (Y/N) ").lower().strip()
                    if pqc == "y":
                        print("oka")
                        linebreak()
                    elif pqc == "n":
                        print("oka")
                        linebreak()
                        break
                    else:
                        print(f"--> Error: '{pqc}' is an invalid prompt answer!")
            elif quiz_choice == "hard":
                while True:
                    hardquiz()
                    pqc = input("do you want to go again? (Y/N) ").lower().strip()
                    if pqc == "y":
                        print("oka")
                    elif pqc == "n":
                        print("oka")
                        break
                    else:
                        print(f"--> Error: '{pqc}' is an invalid prompt answer!")
            elif quiz_choice == "quit":
                print("oka")
                linebreak()
                break
            else: 
                print(f"--> Error: '{quiz_choice}' is an invalid prompt answer!")
    else: 
        print(f"--> Error: '{choice1}' is an invalid prompt answer!")


