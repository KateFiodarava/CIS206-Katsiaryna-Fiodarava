class HealthcareProvider:
    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty

    def get_name(self):
        return self.name
