import os
FILENAME = "students.txt"
def load_students():
    data = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",", 2)
                if len(parts) == 3: data[parts[0]] = [parts[1], parts[2]]
    return data
def save_students(data):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for roll, values in data.items(): f.write(f"{roll},{values[0]},{values[1]}\n")
def add_student(data):
    roll = input("Roll number: ").strip()
    if not roll or roll in data: print("Invalid or duplicate roll number."); return
    name = input("Student name: ").strip()
    try:
        marks = float(input("Marks: "))
        if not name or not 0 <= marks <= 100: print("Invalid name or marks."); return
        data[roll] = [name, str(marks)]; save_students(data); print("Student added.")
    except ValueError: print("Marks must be numeric.")
def display_students(data):
    for roll, values in data.items(): print(roll, values[0], values[1])
    if not data: print("No student records found.")
def search_student(data):
    roll = input("Roll number to search: ")
    print(data.get(roll, "Student not found."))
def update_student(data):
    roll = input("Roll number to update: ")
    if roll not in data: print("Student not found."); return
    name = input("New name: ")
    try:
        marks = float(input("New marks: "))
        if not name or not 0 <= marks <= 100: print("Invalid data."); return
        data[roll] = [name, str(marks)]; save_students(data); print("Updated.")
    except ValueError: print("Marks must be numeric.")
if __name__ == "__main__":
    students = load_students()
    while True:
        c = input("\n1.Add 2.Display 3.Search 4.Update 5.Exit: ")
        if c == "1": add_student(students)
        elif c == "2": display_students(students)
        elif c == "3": search_student(students)
        elif c == "4": update_student(students)
        elif c == "5": break
        else: print("Invalid choice")
