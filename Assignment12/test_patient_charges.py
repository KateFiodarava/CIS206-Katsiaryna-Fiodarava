from patient import Patient
from procedure import Procedure
from datetime import date


patient1 = Patient(
    "John", "A.", "Doe",
    "123 Main St", "Phoenix", "AZ", "85001",
    "602-555-1234",
    "Jane Doe", "602-555-5678"
)


today = date.today().strftime("%Y-%m-%d")

proc1 = Procedure("Physical Exam", today, "Dr. Irvine", 250.00)
proc2 = Procedure("X-ray", today, "Dr. Jamison", 500.00)
proc3 = Procedure("Blood test", today, "Dr. Smith", 200.00)

procedures = [proc1, proc2, proc3]


print("Patient Information")
print("Name:", patient1.get_full_name())
print("Address:", patient1.get_address())
print("Phone:", patient1.get_phone())
print("Emergency Contact:", patient1.get_emergency_contact())
print()


total = 0
print("Procedures:")
for p in procedures:
    print("Procedure:", p.get_name())
    print("Date:", p.get_date())
    print("Practitioner:", p.get_practitioner())
    print("Charge: $", p.get_charge())
    print()
    total += p.get_charge()


print("Total Charges: $", total)
