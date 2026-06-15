# Day 1 (05/29/26):
# Grade Calculator

print("give 5 grades (in %) to avg")
g1 = float(input("Grade 1:"))
g2 = float(input("Grade 2:"))
g3 = float(input("Grade 3:"))
g4 = float(input("Grade 4:"))
g5 = float(input("Grade 5:"))

total = (g1+g2+g3+g4+g5)/5
print(total)

if total > 90:
    print("that results in a A")
elif total >= 80:
    print("that results in a B")
elif total >= 70:
    print("that results in a C")
elif total >= 60:
    print("that results in a D")
else: 
    print("that results in a F")
