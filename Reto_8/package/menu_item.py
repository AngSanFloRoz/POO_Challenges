class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_total(self) -> float:
        raise NotImplementedError(
            "Subclasses must implement calculate_total()"
        )

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_price(self, price: float) -> None:
        self.price = price

    def get_price(self) -> float:
        return self.price