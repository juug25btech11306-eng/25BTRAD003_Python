from storage import load_data, save_data

FILE = "patients.json"

def register_patient():
    patients = load_data(FILE)
    patient_id = max([p["id"] for p in patients], default=1000) + 1

    print("\n--- Patient Registration ---")
    name = input("Patient name: ").strip()
    age_text = input("Age: ").strip()
    gender = input("Gender: ").strip()
    phone = input("Phone number: ").strip()
    problem = input("Health problem: ").strip()

    if not name or not age_text.isdigit() or int(age_text) <= 0:
        print("Please enter a valid name and age.")
        return

    patient = {
        "id": patient_id,
        "name": name,
        "age": int(age_text),
        "gender": gender,
        "phone": phone,
        "problem": problem
    }
    patients.append(patient)
    save_data(FILE, patients)
    print(f"Patient registered successfully. Patient ID: {patient_id}")

def view_patients():
    patients = load_data(FILE)
    print("\n--- Patient List ---")
    if not patients:
        print("No patient records found.")
        return
    for p in patients:
        print(f'ID: {p["id"]} | Name: {p["name"]} | Age: {p["age"]} | '
              f'Gender: {p["gender"]} | Phone: {p["phone"]} | Problem: {p["problem"]}')

def search_patient():
    patients = load_data(FILE)
    search_id = input("Enter patient ID: ").strip()
    if not search_id.isdigit():
        print("Patient ID must be a number.")
        return
    for p in patients:
        if p["id"] == int(search_id):
            print("\nPatient found:")
            for key, value in p.items():
                print(f"{key.title()}: {value}")
            return
    print("Patient not found.")
