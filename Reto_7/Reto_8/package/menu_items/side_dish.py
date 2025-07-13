from menu_item import MenuItem

class SideDish(MenuItem):
    def __init__(self, name: str, price: float, type_of_side: str):
        super().__init__(name, price)
        self.type_of_side = type_of_side

    def set_type_of_side(self, type_of_side: str) -> None:
        self.type_of_side = type_of_side

    def get_type_of_side(self) -> str:
        return self.type_of_side

    def calculate_total(self) -> float:
        return self.price