class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone, emergency_name, emergency_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone

    # Accessor methods
    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    def get_address(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"

    def get_phone(self):
        return self.phone

    def get_emergency_contact(self):
        return f"{self.emergency_name} - {self.emergency_phone}"
