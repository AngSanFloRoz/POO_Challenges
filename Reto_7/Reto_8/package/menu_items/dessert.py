from menu_item import MenuItem

class Dessert(MenuItem):
    def __init__(self, name: str, price: float, calories: int):
        super().__init__(name, price)
        self.calories = calories

    def set_calories(self, calories: int) -> None:
        self.calories = calories

    def get_calories(self) -> int:
        return self.calories

    def calculate_total(self) -> float:
        if self.calories > 500:
            return self.price * 0.8
        return self.price