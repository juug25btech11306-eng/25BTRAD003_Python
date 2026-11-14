from datetime import datetime

students = {}

def get_date():
    while True:
        value = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            return datetime.strptime(value, "%Y-%m-%d").date().isoformat()
        except ValueError:
            print("Invalid date! Use YYYY-MM-DD format.")

def find_student(name):
    return next((student for student in students if student.lower() == name.lower()), None)

def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty!")
    elif find_student(name):
        print("Student already exists!")
    else:
        students[name] = {}
        print(f"Student '{name}' added successfully!")

def remove_student():
    name = input("Enter student name to remove: ").strip()
    actual_name = find_student(name)
    if actual_name:
        del students[actual_name]
        print("Student removed successfully!")
    else:
        print("Student not found!")

def mark_attendance():
    name = input("Enter student name: ").strip()
    actual_name = find_student(name)
    if actual_name is None:
        print("Student not found! Add the student first.")
        return

    attendance_date = get_date()
    print("1. Present")
    print("2. Absent")
    choice = input("Enter attendance status: ")

    if choice == "1":
        status = "Present"
    elif choice == "2":
        status = "Absent"
    else:
        print("Invalid attendance choice!")
        return

    students[actual_name][attendance_date] = status
    print("Attendance saved successfully!")

def individual_report():
    name = input("Enter student name: ").strip()
    actual_name = find_student(name)
    if actual_name is None:
        print("Student not found!")
        return

    records = students[actual_name]
    print("\n----- INDIVIDUAL ATTENDANCE REPORT -----")
    print("Student Name:", actual_name)
    if not records:
        print("No attendance records available.")
        return

    for attendance_date, status in sorted(records.items()):
        print(attendance_date, ":", status)

    total = len(records)
    present = sum(status == "Present" for status in records.values())
    absent = total - present
    print("---------------------------------------")
    print("Total Classes:", total)
    print("Present:", present)
    print("Absent:", absent)
    print("Attendance Percentage:", round(present / total * 100, 2), "%")

def class_report():
    print("\n========== CLASS ATTENDANCE REPORT ==========")
    if not students:
        print("No student records available.")
        return

    print(f"{'Student':<20}{'Total':<10}{'Present':<10}{'Absent':<10}{'Percentage':<12}")
    print("-" * 62)
    for name, records in students.items():
        total = len(records)
        present = sum(status == "Present" for status in records.values())
        absent = total - present
        percentage = (present / total * 100) if total else 0
        print(f"{name:<20}{total:<10}{present:<10}{absent:<10}{percentage:.2f}%")
    print("=" * 62)

def calculate_percentage():
    print("\n----- ATTENDANCE PERCENTAGES -----")
    if not students:
        print("No student records available.")
        return
    for name, records in students.items():
        total = len(records)
        present = sum(status == "Present" for status in records.values())
        percentage = (present / total * 100) if total else 0
        print(f"{name}: {percentage:.2f}%")

def check_shortage():
    if not students:
        print("No student records available.")
        return

    while True:
        try:
            threshold = float(input("Enter minimum attendance percentage (0-100): "))
            if 0 <= threshold <= 100:
                break
            print("Enter a value between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"\nStudents below {threshold}% attendance:")
    found = False
    for name, records in students.items():
        total = len(records)
        present = sum(status == "Present" for status in records.values())
        percentage = (present / total * 100) if total else 0
        if percentage < threshold:
            print(f"{name}: {percentage:.2f}%")
            found = True
    if not found:
        print("No students are below the threshold.")

def class_statistics():
    total_students = len(students)
    total_classes = sum(len(records) for records in students.values())
    total_present = sum(
        sum(status == "Present" for status in records.values())
        for records in students.values()
    )
    total_absent = total_classes - total_present
    print("\n----- CLASS STATISTICS -----")
    print("Total Students:", total_students)
    print("Total Attendance Entries:", total_classes)
    print("Total Present Entries:", total_present)
    print("Total Absent Entries:", total_absent)
    percentage = total_present / total_classes * 100 if total_classes else 0
    print("Overall Attendance:", round(percentage, 2), "%")

def main():
    while True:
        print("\n===================================")
        print("        ATTENDANCE TRACKER")
        print("===================================")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Mark / Update Attendance")
        print("4. Individual Attendance Report")
        print("5. Complete Class Report")
        print("6. Calculate Attendance Percentage")
        print("7. Check Attendance Shortage")
        print("8. Class Statistics")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            mark_attendance()
        elif choice == "4":
            individual_report()
        elif choice == "5":
            class_report()
        elif choice == "6":
            calculate_percentage()
        elif choice == "7":
            check_shortage()
        elif choice == "8":
            class_statistics()
        elif choice == "9":
            print("Thank you for using Attendance Tracker!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
