# Day 6 (06/04/26):
# a final grade calculator .

while True:
    try:
        grade_input = input("Enter your current grade in your course: (eg. 45% = 45, 60.10% = 60.10) ")
        grade = float(grade_input)

        if not (0 < grade <= 100):
            print(f"--> Error: {grade} is a invalid grade, your grade should be BETWEEN 0, and 100.")
            print("\n")
            continue

        weight_input = input("enter the weight of the final in your course: (in decimal eg. 0.2 = 20%) ")
        weight = float(weight_input)

        if not (0 < weight <= 1):
            print(f"--> Error: {weight} is a invalid weight, your weightshould be between 0, and 1.")
            print("\n")
            continue
        if weight == 0:
            print("--> Error: your weight has to be BETWEEN 0 and 1, pick a different weight (your weight couldnt be 0 anyways unless it was a pre-test)")
            print("\n")
            continue

        goal_input = input("what grade would you want to have in the course overall: (eg. 98% = 98, 86.78% = 86.78) ")
        g_grade = float(goal_input)
        
        break
    except ValueError:
        print("--> Error: Your answer MUST be in decimals/integers. Try again.\n")


# Defining the calculation function using the validated variables
def finalgradecalculation():
    # formula: Required = (Goal − Current × (100% − Final Weight)) / Final Weight
    d_grade = (g_grade - grade * (1 - weight)) / weight
    rounded_finalgrade = round(d_grade, 2)
    return rounded_finalgrade

required_grade = finalgradecalculation()
message = ""

print("\n")

if required_grade >= 100:
    message = "(is there extra credit?)"
elif required_grade >= 90:
    message = "(uhhh)"
elif required_grade >= 80:
    message = "(you better hope theres a massive curve on the test)"
elif required_grade >= 70:
    message = "(you might want to lock in, its still definitely possible!)"
elif required_grade >= 60:
    message = "(your chilling if you atleast are decent in the test material)"
elif required_grade >= 50:
    message = "(all you need is to get nearly more than half correct, shouldnt be that bad)"
elif required_grade >= 40:
    message = "(i would say you are fine, dw)"
elif required_grade >= 30:
    message = "(you are more than fine, just dont fumble)"
elif required_grade >= 20:
    message = f"(might aswell not try, cause you are almost certained to get a {g_grade}%)"
elif required_grade >= 10:
    message = "(all of the studying definitely paid off, right?)"
elif required_grade > 0:
    message = "(just sleep, you are fine lol)"
elif required_grade <= 0:
    message = "(you are the most chill you could possibly be rn, just dont show up to school atp)"
    
print(f"you must need a grade of atleast a {required_grade}% to pass your specific course. {message}")
