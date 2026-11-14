students = {}
for _ in range(int(input("Number of students: "))):
    name = input("Student name: ")
    marks = float(input("Marks (0-100): "))
    while not 0 <= marks <= 100:
        marks = float(input("Enter marks from 0 to 100: "))
    students[name] = marks
for name, marks in students.items():
    grade = "A" if marks >= 90 else "B" if marks >= 80 else "C" if marks >= 70 else "D" if marks >= 60 else "E" if marks >= 40 else "F"
    print(name, marks, grade, "Pass" if marks >= 40 else "Fail")
