class PaymentMethod:
    def __init__(self):
        pass

    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")