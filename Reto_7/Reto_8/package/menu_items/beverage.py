from menu_item import MenuItem

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size: str):
        super().__init__(name, price)
        self.size = size

    def set_size(self, size: str) -> None:
        self.size = size

    def get_size(self) -> str:
        return self.size

    def calculate_total(self) -> float:
        return self.price