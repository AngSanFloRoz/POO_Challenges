from menu_item import MenuItem

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, with_soup: bool):
        super().__init__(name, price)
        self.with_soup = with_soup

    def set_with_soup(self, with_soup: bool) -> None:
        self.with_soup = with_soup

    def get_with_soup(self) -> bool:
        return self.with_soup

    def calculate_total(self) -> float:
        if self.with_soup:
            return self.price + 4
        else:
            return self.price