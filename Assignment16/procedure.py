class Procedure:
    def __init__(self, name, date, charge):
        self.name = name
        self.date = date
        self.charge = charge

    def to_dict(self):
        return {
            "name": self.name,
            "date": self.date,
            "charge": self.charge
        }

    @staticmethod
    def from_dict(data):
        return Procedure(data["name"], data["date"], data["charge"])
