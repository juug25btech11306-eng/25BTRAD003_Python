from storage import load_data, save_data
from doctor import DOCTORS

FILE = "appointments.json"

def book_appointment():
    patients = load_data("patients.json")
    if not patients:
        print("Register a patient before booking an appointment.")
        return

    print("\n--- Book Appointment ---")
    patient_text = input("Enter patient ID: ").strip()
    if not patient_text.isdigit():
        print("Invalid patient ID.")
        return
    patient = next((p for p in patients if p["id"] == int(patient_text)), None)
    if patient is None:
        print("Patient not found.")
        return

    for doctor in DOCTORS:
        print(f'{doctor["id"]}. {doctor["name"]} - {doctor["specialization"]}')
    doctor_text = input("Choose doctor ID: ").strip()
    if not doctor_text.isdigit():
        print("Invalid doctor ID.")
        return
    doctor = next((d for d in DOCTORS if d["id"] == int(doctor_text)), None)
    if doctor is None:
        print("Doctor not found.")
        return

    date = input("Appointment date (DD-MM-YYYY): ").strip()
    time = input("Appointment time: ").strip()
    if not date or not time:
        print("Date and time are required.")
        return

    appointments = load_data(FILE)
    appointment_id = max([a["id"] for a in appointments], default=0) + 1
    appointments.append({
        "id": appointment_id,
        "patient_id": patient["id"],
        "patient_name": patient["name"],
        "doctor": doctor["name"],
        "date": date,
        "time": time
    })
    save_data(FILE, appointments)
    print(f"Appointment booked successfully. Appointment ID: {appointment_id}")

def view_appointments():
    appointments = load_data(FILE)
    print("\n--- Appointment List ---")
    if not appointments:
        print("No appointments found.")
        return
    for a in appointments:
        print(f'ID: {a["id"]} | Patient: {a["patient_name"]} '
              f'(ID {a["patient_id"]}) | Doctor: {a["doctor"]} | '
              f'Date: {a["date"]} | Time: {a["time"]}')
