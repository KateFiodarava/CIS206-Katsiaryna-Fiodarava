import json
from procedure import Procedure
from billing import Billing

class Patient:
    def __init__(self, first_name, last_name, address, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.procedures = []
        self.billings = []

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def add_visit(self, procedure, billing):
        self.procedures.append(procedure)
        self.billings.append(billing)

    def save_to_file(self, filename):
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "phone": self.phone,
            "procedures": [p.to_dict() for p in self.procedures],
            "billings": [b.to_dict() for b in self.billings]
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_from_file(filename):
        with open(filename, "r") as file:
            data = json.load(file)

        patient = Patient(data["first_name"], data["last_name"], data["address"], data["phone"])

        for proc_data, bill_data in zip(data["procedures"], data["billings"]):
            procedure = Procedure.from_dict(proc_data)
            billing = Billing.from_dict(bill_data)
            patient.add_visit(procedure, billing)

        return patient
