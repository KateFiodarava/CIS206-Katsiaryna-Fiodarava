class Billing:
    def __init__(self, amount, paid=False):
        self.amount = amount
        self.paid = paid

    def to_dict(self):
        return {
            "amount": self.amount,
            "paid": self.paid
        }

    @staticmethod
    def from_dict(data):
        return Billing(data["amount"], data["paid"])
