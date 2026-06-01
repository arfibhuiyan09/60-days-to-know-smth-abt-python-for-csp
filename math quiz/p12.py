# Day 4 (06/01/26):
# math quiz revamped to be acceptable for AP CSP CT
import random

print("math quiz:")
choice = input("do you want to play (Y/N)").lower()

questions = ["What is 2-3", 
             "What is (2)^2 - 4", 
             "What is (10)/(2)^2 + sqrt(64)/2", 
             "simplify: 2^(2x) - 4^x - 32", 
             "simpify (1/sin(x)) * cscx * tanx in terms only with cosine in the first quadrant of the Unit Circle"]

Q5approved_answers = ["(1/(cos(x)(sqrt(1-cos^2(x)))", 
                      "1/(cos(x)*sqrt(1-cos^2(x)))", 
                      "1/(cos(x)(sqrt(1-cos^2(x))))"]

answers = [["-1"],
           ["0"],
           ["6.5"],
           ["-32"],
           Q5approved_answers]

def quiz():
    count = 0
    for i, question in enumerate(questions):
        print(question)
        answer = input("answer the question:").lower()
        if answer in answers[i]:
            print("good job")
            count += 1
        else:
            print("no")
    percentage = (count / len(questions)) * 100
    print(f"you have gotten {count}/{len(questions)} correct, which is a {percentage}%!")
    

if choice == "y":
    while True:
        quiz()
elif choice == "n":
    print("oka")
else:
    print("invalid option")