from menu_item import MenuItem

class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, taste: str):
        super().__init__(name, price)
        self.taste = taste

    def set_taste(self, taste: str) -> None:
        self.taste = taste

    def get_taste(self) -> str:
        return self.taste

    def calculate_total(self) -> float:
        return self.price