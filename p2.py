while True:
    print("do you want to add, subtract, multiply, or divide?")
    choice = input().lower()

    if choice == "add":
        print("choose two numbers to add")
        num1 = float(input("number 1:  "))
        num2 = float(input("number 1:  "))
        total_add = (num1 + num2)
        print("the answer is " + str(total_add))

    elif choice == "subtract":
        print("choose two numbers to subtract")
        num1 = float(input("number 1:  "))
        num2 = float(input("number 1:  "))
        total_sub = (num1 - num2)
        print("the answer is " + str(total_sub))

    elif choice == "multiply":
        print("choose two numbers to multiply")
        num1 = float(input("number 1:  "))
        num2 = float(input("number 1:  "))
        total_mul = (num1 * num2)
        print("the answer is " + str(total_mul))

    elif choice == "divide":
        print("choose two numbers to divide")
        num1 = float(input("number 1:  "))
        num2 = float(input("number 1:  "))
        total_div = (num1 / num2)
        print("the answer is " + str(total_div))

    print("want to try again with a different calculation")
    affimation = input().lower()

    if affimation != "yes":
        print("oka")
        break