#math diagostic test
#Day 8-9: (6/6-7/26)

import time

arithmetic_dict = {
    "What is 7 + 5? (answer: integer only)": "12",
    "What is 18 - 4? (answer: integer only)": "14",
    "What is 12 ÷ 3? (answer: integer only, use /)": "4",
    "What is 4.5 + 2.5? (decimal allowed, no units)": "7",
    "Evaluate: 6 * (10 - 2) (integer only)": "48"
}

algebra_dict = {
    "Solve for x: 2x - 10 = 12 (integer only)": "11",
    "Find the slope of y = 4(x - 2) + 5 (integer only)": "4",
    "Solve for x: 4(x - 2) + 5 = 17 (integer only)": "5",
    "Evaluate: log base 5 of 5 (integer only)": "1",
    "Solve: e^(2x) - e^x - 12 = 0 (answer in form ln(answer))": "ln(4)"
}

geometry_dict = {
    "Right triangle ABC: AB = 3, BC = 4. Find AC (integer only)": "5",
    "In a figure ABCD, if AB || CD and AC || BD, is it a square? (yes or no)": "no",
    "Point (10,0) is shifted left 10, up 2, then dilated by 1/5 about origin. What is x-coordinate? (integer only)": "0",
    "Trapezoid ABCD: AB = 5, CD is twice AB. Find CD (integer only)": "10",
    "Given angles: a = 45°, a ≅ c, c + d = 180°. Find c (integer only, no degree symbol)": "45"
}

trigonometry_dict = {
    "Evaluate sin(π/6) (fraction only, e.g. 1/2)": "1/2",
    "Law of Sines: A = 30°, B = 45°, a = 12. Find b (round to 2 decimals)": "16.97",
    "Is x = π/4 in domain of f(x) = 0.5sin(x) on [-π/2, π/2]? (yes or no)": "yes",
    "evaluate this student's response to answering the question 2sin^2(x)-sin(x)+5=8: \n \n Step 1: 2sin^2(x)-sin(x)-3=0, Step 2: (2u^2)-u-3=0, Step 3: (2u+3)=0 and (u-1)=0, Step 4: u=(-3/2), u=1, Step 5: sin(x)=(sqrt(3))/2, sin(x)=1, Step 6: x=pi/3, 2pi/3, pi/2. \n \n Is this student correct? if not, which step did they mess up at. (Write 'none' or 'step x')": "step 5",
    "Solve sin(x) + cos(x) = √2 on (0, π) (degrees only, no symbol)": "45"
}

calculus_dict = {
    "What is the derivative of x^2? (expression form)": "2x",
    "Find the area under the curve of x^4 - 2x^2 from [0,6] (round to 1 decimal)": "1411.2",
    "Assume x = t/2. Find t such that derivative of -(x-6)^2 is 0": "12",
    "Evaluate: ∫₀² (2x)(x^2 + 7)^4 dx (fraction form)": "144244/5",
    "Determine convergence of Σ n²/(n³ + 4): write 'converges' or 'diverges'": "diverges"
}


def arithmetic():
    arithmeticcount = 0

    for question, answer in arithmetic_dict.items():
        user_input = input(f"{question} ").strip().lower()

        if user_input == answer.lower():
            print("correct")
            arithmeticcount += 1
        else:
            print("no")

    return arithmeticcount

def algebra():
    algebracount = 0

    for question, answer in algebra_dict.items():
        user_input = input(f"{question} ").strip().lower()

        if user_input == answer.lower():
            print("correct")
            algebracount += 1
        else:
            print("no")

    return algebracount 


def geometry():
    geometrycount = 0

    for question, answer in geometry_dict.items():
        user_input = input(f"{question} ").strip().lower()

        if user_input == answer.lower():
            print("correct")
            geometrycount += 1
        else:
            print("no")

    return geometrycount


def trigonometry():
    trigonometrycount = 0

    for question, answer in trigonometry_dict.items():
        user_input = input(f"{question} ").strip().lower()

        if user_input == answer.lower():
            print("correct")
            trigonometrycount += 1
        else:
            print("no")

    return trigonometrycount 


def calculus():
    calculuscount = 0

    for question, answer in calculus_dict.items():
        user_input = input(f"{question} ").strip().lower()

        if user_input == answer.lower():
            print("correct")
            calculuscount += 1
        else:
            print("no")

    return calculuscount

def runskillcheck():
    print("ok first its time to test your skill on arithmetic: \n")

    arithmetic_score = arithmetic()

    print("ok now algebra: \n")

    algebra_score = algebra()

    print("next, geometry: \n")

    geometry_score = geometry()


    print("next, trigonometry: \n")

    trigonometry_score = trigonometry()

    print("and finally, calculus! \n")

    calculus_score = calculus()

    #---------score calculation------------

    total_questions = len(arithmetic_dict) + len(algebra_dict) + len(geometry_dict) + len(trigonometry_dict) + len(calculus_dict)
    raw_score = (arithmetic_score + algebra_score + geometry_score + trigonometry_score + calculus_score)
    percentage = (raw_score / total_questions) * 100

    print("ok let me calculate all of your answers:")
    time.sleep(1)
    print("loading...")
    time.sleep(2)
    print(f"ok so you got a raw score of {raw_score}/{total_questions} which equates to a {percentage}.")
    print(f"You got {arithmetic_score}/{len(arithmetic_dict)} correct in arithmetic.")
    print(f"You got {algebra_score}/{len(algebra_dict)} correct in algebra.")
    print(f"You got {geometry_score}/{len(geometry_dict)} correct in geometry.")
    print(f"You got {trigonometry_score}/{len(trigonometry_dict)} correct in trigonometry.")
    print(f"You got {calculus_score}/{len(calculus_dict)} correct in calculus. \n")

    grade = int(input("one last thing, what grade are you enrolled as right now? (just enter the grade number like 10, if you are in university, enter 13-16)").strip())
    if grade <= 5:
        expected_percentage = 25
        if percentage > expected_percentage:
            print(f"the percentage average of pupil taking this test around your age is {expected_percentage}%. You got a {percentage}% which is a difference of {percentage - expected_percentage}%")
            print("\nthat was a really challenging set involving trigonometry AND calculus AND you scored above grade level, Good job!!")
        else:
            print(f"the percentage average of pupil taking this test around your age is {expected_percentage}%. You got a {percentage}% which is a difference of {percentage - expected_percentage}%")
            print("\nthat was a really challenging set involving trigonometry AND calculus, scoring below grade level is okay since you probably havent even seen the topics tested here, Good job!!")

    elif grade <= 8:
        expected_percentage = 45
        if percentage > expected_percentage:
            print(f"the percentage average of pupil taking this test around your age is {expected_percentage}%. You got a {percentage}% which is a difference of {percentage - expected_percentage}%")
            print(f"\nwow you being in {grade} AND scoring a {percentage}% is above grade level! Good job!!")
        else:
            print(f"the percentage average of pupil taking this test around your age is {expected_percentage}%. You got a {percentage}% which is a difference of {percentage - expected_percentage}%")
            print("\ndont worry, this diagnostic took math from arithmetic to calculus, since you have been only exposed to arithmetic and algebra, scoring below grade level is okay! you will learn these topics in about 4-5 years or so.")

    elif grade <= 10:
        expected_percentage = 65
        if percentage > expected_percentage:
            print(f"the percentage average of pupil taking this test around your age is {expected_percentage}%. You got a {percentage}% which is a difference of {percentage - expected_percentage}%")
            print(f"\nas a {grade}th grader, this is about the average, you probably know algebra 2 and or calculus AND scoring a {percentage}% is expected, regarless you're above grade level so Good job!!")
        else:
            print(f"the percentage average of pupil taking this test around your age is {expected_percentage}%. You got a {percentage}% which is a difference of {percentage - expected_percentage}%")
            print("\nassuming you have taken algebra 2 and not calculus yet, this makes sense, make sure to get ready for Calculus because calculus doesnt tread lightly to newbies. regardless, good job tho!")

    else:
        expected_percentage = 85
        if percentage > expected_percentage:
            print(f"the percentage average of pupil taking this test around your age is {expected_percentage}%. You got a {percentage}% which is a difference of {percentage - expected_percentage}%")
            print(f"\nas being a university student, scoring a {percentage}% is expected, hope calculus is going well for you thus far!")
        else:
            print(f"the percentage average of pupil taking this test around your age is {expected_percentage}%. You got a {percentage}% which is a difference of {percentage - expected_percentage}%")
            print(f"\nyou probably didnt go to university and didnt learn calculus, which is why you got a {percentage}% and not {expected_percentage}% (the percentage average of pupil taking this test around your age). It is fine if you are working somewhere and not in university. If you are in uni tho, good luck.")

print("have you ever wondered to yourself how much math you've actually learned, throughout school/university?")
choice = input("well, do you want to take a 'skill test' to see how much math you actually know? (Y/N)  ").lower().strip()

while True:
    if choice == "y":
        runskillcheck()
        break
    elif choice == "n":
        print("oka")
    else:
        print(f"--> Error: '{choice}' is an invalid prompt answer!")
