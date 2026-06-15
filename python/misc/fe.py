print("math quiz:")
choice = input("do you want to play (Y/N)").lower()
count = 0
questions = ["What is 2-3", "What is (2)^2 - 4", "What is (10)/(2)^2 + sqrt(64)/2", "simplify: 2^(2x) - 4^x - 32", "simpify (1/sin(x)) * cscx * tanx in terms only with cosine in the first quadrant of the Unit Circle"]
Q5approved_answers = ["(1/(cos(x)(sqrt(1-cos^2(x)))", "1/(cos(x)*sqrt(1-cos^2(x)))", "1/(cos(x)(sqrt(1-cos^2(x))))"]
answers = [["-1"], ["0"], ["6.5"], ["-32"], Q5approved_answers]
if choice == "y":
    for i, question in enumerate(questions):
        print(question)
        answer = input("answer the question:").lower()
        if answer in answers[i]:
            print("good job")
        else:
            print("no")