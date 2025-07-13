from package.payment_method import PaymentMethod

class CashPayment(PaymentMethod):
    def __init__(self, amount_provided):
        super().__init__()
        self.amount_provided = amount_provided

    def pay(self, amount):
        if self.amount_provided >= amount:
            print(
                f"Payment made in cash. "
                f"Change: ${self.amount_provided - amount:.2f}"
            )
        else:
            print(
                f"Insufficient funds. "
                f"${amount - self.amount_provided:.2f} more needed."
            )