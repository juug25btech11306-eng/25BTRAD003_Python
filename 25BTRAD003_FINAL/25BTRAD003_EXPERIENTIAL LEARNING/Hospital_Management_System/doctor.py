DOCTORS = [
    {"id": 1, "name": "Dr. Arun", "specialization": "General Physician"},
    {"id": 2, "name": "Dr. Priya", "specialization": "Cardiologist"},
    {"id": 3, "name": "Dr. Kumar", "specialization": "Pediatrician"},
    {"id": 4, "name": "Dr. Sneha", "specialization": "Dermatologist"}
]

def view_doctors():
    print("\n--- Available Doctors ---")
    for doctor in DOCTORS:
        print(f'ID: {doctor["id"]} | {doctor["name"]} | '
              f'Specialization: {doctor["specialization"]}')
