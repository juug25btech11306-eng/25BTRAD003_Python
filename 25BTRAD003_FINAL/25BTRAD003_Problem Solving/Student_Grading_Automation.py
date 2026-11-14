name = input("Enter student name: ")
marks = float(input("Enter marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
elif marks >= 40:
    grade = "E"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Marks:", marks)
print("Grade:", grade)

if marks >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
