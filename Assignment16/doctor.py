from healthcare_provider import HealthcareProvider

class Doctor(HealthcareProvider):
    def __init__(self, id, name, specialty, specialization):
        super().__init__(id, name, specialty)
        self.specialization = specialization

    def perform_procedure(self, procedure):
        print(f"Dr. {self.name} is performing {procedure.name}")
