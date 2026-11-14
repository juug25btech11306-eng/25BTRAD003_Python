def create_bill():
    print("\n--- Hospital Billing ---")
    patient_name = input("Patient name: ").strip()
    if not patient_name:
        print("Patient name is required.")
        return

    try:
        consultation = float(input("Consultation fee (Rs.): "))
        medicine = float(input("Medicine charges (Rs.): "))
        tests = float(input("Test charges (Rs.): "))
        if min(consultation, medicine, tests) < 0:
            raise ValueError
    except ValueError:
        print("Enter valid non-negative amounts.")
        return

    total = consultation + medicine + tests
    print("\n========== BILL ==========")
    print(f"Patient: {patient_name}")
    print(f"Consultation: Rs. {consultation:.2f}")
    print(f"Medicine:     Rs. {medicine:.2f}")
    print(f"Tests:        Rs. {tests:.2f}")
    print("--------------------------")
    print(f"Total amount: Rs. {total:.2f}")
    print("==========================")
