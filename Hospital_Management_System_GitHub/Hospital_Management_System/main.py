from patient import register_patient, view_patients, search_patient
from doctor import view_doctors
from appointment import book_appointment, view_appointments
from billing import create_bill

def show_menu():
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Register Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. View Doctors")
    print("5. Book Appointment")
    print("6. View Appointments")
    print("7. Generate Patient Bill")
    print("8. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            register_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            view_doctors()
        elif choice == "5":
            book_appointment()
        elif choice == "6":
            view_appointments()
        elif choice == "7":
            create_bill()
        elif choice == "8":
            print("Thank you for using the Hospital Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()
