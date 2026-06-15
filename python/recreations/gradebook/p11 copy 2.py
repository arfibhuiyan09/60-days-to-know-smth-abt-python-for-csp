# Day 4: 06/01/26
#gradebook (dictionaries)

students = {}
choice=0
choice1=0

    
def add():
    student = input("who else do you want to add to your gradebook? ")
    grade = float(input("what is their grade? "))
    students.update({student: grade})

def update():
    student = input("who do you want to update in your gradebook ")
    grade = float(input("what is their grade? "))
    students.update({student: grade})

def remove():
    while True:
        student = input("Who do you want to remove from your gradebook?")
        if student in students:
            students.pop(student)
            break
        else:
            print(f"--> Error: '{student}' wasnt found in the gradebook!")
            break
    
def view():
    gradebook = students.items()
    print("Gradebook: \n ")
    for student, grade in gradebook:
        print(f"{student}: {grade}")



while True:
    choice = input("Do you want to input grades into a gradebook for students? (Y/N) ").lower().strip()
    if choice == "y":
        student = input("Enter the name of a student you want to put in the gradebook:   ")
        grade = float(input(f"Enter the grade of {student}:   "))
        students.update({student: grade})
        while True:
            last_student_added = list(students.keys())[-1]
            choice1 = input(f"you have {last_student_added} in your roster. Do you want to add another student (add), update grades (update), remove a student (remove), view the entire roster (view), or quit entirely (quit)?  ").lower().strip()
            if choice1 == "add":
                add()
            elif choice1 == "update":
                update()
            elif choice1 == "remove":
                try:
                    last_student_added = list(students.keys())[-1]
                except: IndexError
                print("null")
                remove()
            elif choice1 == "view":
                view()
            elif choice1 == "quit":
                print("oka")
                break
            else:
                print(f"--> Error: '{choice1}' is an invalid prompt answer!")
    elif choice == "n":
        print("oka")
        break
    else:
        print(f"--> Error: '{choice1}' is an invalid prompt answer!")