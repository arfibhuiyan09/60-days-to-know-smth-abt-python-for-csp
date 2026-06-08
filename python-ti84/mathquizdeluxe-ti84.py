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
"evaluate this student's response to 2sin^2(x)-sin(x)+5=8 and identify error step": "step 5",
"Solve sin(x) + cos(x) = √2 on (0, π) (degrees only, no symbol)": "45"
}

calculus_dict = {
"What is the derivative of x^2? (expression form)": "2x",
"Find the area under the curve of x^4 - 2x^2 from [0,6] (round to 1 decimal)": "1411.2",
"Assume x = t/2. Find t such that derivative of -(x-6)^2 is 0": "12",
"Evaluate: ∫₀² (2x)(x^2 + 7)^4 dx (fraction form)": "144244/5",
"Determine convergence of Σ n²/(n³ + 4): write 'converges' or 'diverges'": "diverges"
}


def ask_section(d):
    score = 0

    for q in d:
        user_input = input(q + " ").strip().lower()

        if user_input == d[q].lower():
            print("correct")
            score += 1
        else:
            print("no")

    return score


def runskillcheck():
    print("arithmetic:\n")
    a = ask_section(arithmetic_dict)

    print("algebra:\n")
    b = ask_section(algebra_dict)

    print("geometry:\n")
    c = ask_section(geometry_dict)

    print("trigonometry:\n")
    d = ask_section(trigonometry_dict)

    print("calculus:\n")
    e = ask_section(calculus_dict)

    total = (
        len(arithmetic_dict) +
        len(algebra_dict) +
        len(geometry_dict) +
        len(trigonometry_dict) +
        len(calculus_dict)
    )

    raw = a + b + c + d + e
    percent = (raw / total) * 100

    print("calculating...")
    time.sleep(1)
    print("loading...")
    time.sleep(2)

    print("score: {}/{} = {}%".format(raw, total, round(percent, 2)))

    grade = int(input("grade level? ").strip())

    if grade <= 5:
        expected = 25
    elif grade <= 8:
        expected = 45
    elif grade <= 10:
        expected = 65
    else:
        expected = 85

    diff = percent - expected

    print("expected: {}%".format(expected))
    print("difference: {}%".format(round(diff, 2)))


# ---------------- MAIN ----------------

print("ever wondered how much math you've learned?")
choice = input("take skill test? (Y/N) ").lower().strip()

while True:
    if choice == "y":
        runskillcheck()
        break

    elif choice == "n":
        print("oka")
        break

    else:
        print("--> Error: '{}' invalid".format(choice))
        break
