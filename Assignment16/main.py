
from patient import Patient
from procedure import Procedure
from billing import Billing

def create_patient():
    first = input("First name: ")
    last = input("Last name: ")
    address = input("Address: ")
    phone = input("Phone: ")

    patient = Patient(first, last, address, phone)

    while True:
        name = input("Procedure name: ")
        date = input("Date (YYYY-MM-DD): ")
        charge = float(input("Charge: "))

        procedure = Procedure(name, date, charge)
        billing = Billing(charge)

        patient.add_visit(procedure, billing)

        more = input("Add another procedure? (y/n): ")
        if more.lower() != 'y':
            break

    return patient

def main():
    print("Welcome to the Healthcare Management System")
    print("1 - Add New Patient")
    print("2 - Load Patient File")
    choice = input("Choose an option: ")

    if choice == "1":
        patient = create_patient()
        filename = input("Save as (e.g. patient1.json): ")
        patient.save_to_file(filename)
        print("Saved successfully!")
    elif choice == "2":
        filename = input("Enter filename: ")
        patient = Patient.load_from_file(filename)
        print(f"\nPatient: {patient.get_full_name()}")
        for i, (p, b) in enumerate(zip(patient.procedures, patient.billings), 1):
            print(f"\nProcedure {i}:")
            print(f"  Name: {p.name}")
            print(f"  Date: {p.date}")
            print(f"  Charge: ${p.charge}")
            print(f"  Paid: {'Yes' if b.paid else 'No'}")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()


