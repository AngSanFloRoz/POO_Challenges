from package.menu_items.dessert import Dessert
from package.menu_items.main_course import MainCourse
from package.menu_items.side_dish import SideDish
from package.menu_items.appetizer import Appetizer
from package.menu_items.beverage import Beverage


class OrderItemsIterator:
    def __init__(self, order):
        self._order = order
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._order.menu_items):
            item = self._order.menu_items[self._index]
            self._index += 1
            result = {
                "name": item.get_name(),
                "price": item.get_price()
            }
            # Agrega el tercer atributo según el tipo de MenuItem
            if isinstance(item, Appetizer):
                result["taste"] = item.get_taste()
            elif isinstance(item, Beverage):
                result["size"] = item.get_size()
            elif isinstance(item, Dessert):
                result["calories"] = item.get_calories()
            elif isinstance(item, MainCourse):
                result["with_soup"] = item.get_with_soup()
            elif isinstance(item, SideDish):
                result["type_of_side"] = item.get_type_of_side()
            return result
        else:
            raise StopIteration