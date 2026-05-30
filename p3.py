#Day 2: 05/30/26
print("math quiz:")
print("do you want to play (Y/N)")
choice = input().lower()
count = 0
if choice == "y":
    print("first question: What is 2-3")
    answer1 = float(input("Answer:  "))
    if answer1 == -1:
        print("good job")
        count += 1
    else: 
        print("wrong answer .")
    print("second question: What is (2)^2 - 4")
    answer2 = float(input("Answer:  "))
    if answer2 == 0:
        print("good job")
        count += 1
    else: 
        print("wrong answer .")
    print("third question: What is (10)/(2)^2 + sqrt(64)/2")
    answer3 = float(input("Answer:  "))
    if answer3 == 6.5:
        print("good job")
        count += 1
    else: 
        print("wrong answer .")
    print("fourth question: simplify: 2^(2x) - 4^x - 32")
    answer4 = float(input("Answer:  "))
    if answer4 == -32:
        print("good job")
        count += 1
    else: 
        print("wrong answer .")
    print("last question: simpify (1/sin(x)) * cscx * tanx in terms only with cosine in the first quadrant of the Unit Circle")
    answer5 = input("Answer:  ").lower()
    Q5approved_answers = ["(1/(cos(x)(sqrt(1-cos^2(x)))", "1/(cos(x)*sqrt(1-cos^2(x)))", "1/(cos(x)(sqrt(1-cos^2(x))))"]
    if answer5 in Q5approved_answers:
        print("good job")
        count += 1
    else: 
        print("wrong answer .")
    if count == 0:
        print("you got 0/5 questions correct which is a 0%. go to https://www.khanacademy.org/math/precalculus and try again.")
    elif count == 1:
        print("you got 1/5 questions correct which is a 20%. Lock in.")
    elif count == 2:
        print("you got 2/5 questions correct which is 40%, ur close to passing. Lock in.")
    elif count == 3:
        print("you got 3/5 questions correct which is 60%, you technically pass, good job")
    elif count == 4:
        print("you got 4/5 questions correct which is 80%, that is not bad, good job!")
    elif count == 5:
        print("you got all 5/5 questions correct which is a 100%, you must be in calculus level, with in consideration of Q5.")
    elif count >= 6:
        print("?")
elif choice == "n":
    print("ok")
else:
    print("i said Y/N, lock in .")
