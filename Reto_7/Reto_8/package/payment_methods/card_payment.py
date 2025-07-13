from package.payment_method import PaymentMethod

class CardPayment(PaymentMethod):
    def __init__(self, card_number, cvv):
        super().__init__()
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount):
        print(
            f"Paying ${amount:.2f} with card "
            f"ending in {self.card_number[-4:]}"
        )