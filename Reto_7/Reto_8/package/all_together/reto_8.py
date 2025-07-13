# reto_8.py

import json
import os
from collections import namedtuple

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

class Order:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item: MenuItem) -> None:
        self.menu_items.append(item)

    def count_items(self) -> tuple:
        num_beverages = 0
        num_appetizers = 0
        num_main_courses = 0
        num_desserts = 0
        num_side_dishes = 0

        for item in self.menu_items:
            if isinstance(item, Beverage):
                num_beverages += 1
            elif isinstance(item, Appetizer):
                num_appetizers += 1
            elif isinstance(item, MainCourse):
                num_main_courses += 1
            elif isinstance(item, Dessert):
                num_desserts += 1
            elif isinstance(item, SideDish):
                num_side_dishes += 1

        return (
            num_beverages,
            num_appetizers,
            num_main_courses,
            num_desserts,
            num_side_dishes
        )

    def calculate_total_bill(self) -> float:
        total = 0
        for item in self.menu_items:
            total += item.calculate_total()
        c = self.count_items()
        if c[0] == 0 and c[2] >= 1 and c[3] >= 2:
            total *= 0.5
        if c[3] >= 5:
            total *= 0.65
        if c[2] >= 2:
            total *= 0.8
        return total

    def __str__(self):
        return (
            f"Order with {len(self.menu_items)} items: "
            f"{[item.get_name() for item in self.menu_items]}"
        )
    

    def create_new_menu(self, name: str, items: list) -> None:
        menu = {
            "name": name,
            "items": [menu_item.__dict__ for menu_item in items]
        }
        file_path = f"{name}.json"
        with open(file_path, 'w') as file:
            json.dump(menu, file, indent=4)
        print(f"Menu '{name}' created and saved to {file_path}")

    def load_menu(self, name: str) -> None:
        file_path = f"{name}.json"
        if not os.path.exists(file_path):
            print(f"Menu '{name}' does not exist.")
            return None
        with open(file_path, 'r') as file:
            menu = json.load(file)
            print(f"Menu '{menu['name']}' loaded with items:")
            for item in menu['items']:
                print(f"- {item['name']} (${item['price']})")

    def delete_menu(self, name: str) -> None:
        file_path = f"{name}.json"
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Menu '{name}' deleted.")
        else:
            print(f"Menu '{name}' does not exist.")

    def add_item_to_menu(self, name: str, item: MenuItem) -> None:
        file_path = f"{name}.json"
        if not os.path.exists(file_path):
            print(f"Menu '{name}' does not exist.")
            return None
        with open(file_path, 'r+') as file:
            menu = json.load(file)
            menu['items'].append(item.__dict__)
            json.dump(menu, file, indent=4)
        print(f"Item '{item.get_name()}' added to menu '{name}'.")

    def update_item_in_menu(self, name: str, item: MenuItem) -> None:
        file_path = f"{name}.json"
        if not os.path.exists(file_path):
            print(f"Menu '{name}' does not exist.")
            return None
        with open(file_path, 'r+') as file:
            menu = json.load(file)
            for i, existing_item in enumerate(menu['items']):
                if existing_item['name'] == item.get_name():
                    menu['items'][i] = item.__dict__
                    break
            else:
                print(f"Item '{item.get_name()}' not found in menu '{name}'.")
                return None
            json.dump(menu, file, indent=4)
        print(f"Item '{item.get_name()}' updated in menu '{name}'.")

    def delete_item_from_menu(self, name: str, item_name: str) -> None:
        file_path = f"{name}.json"
        if not os.path.exists(file_path):
            print(f"Menu '{name}' does not exist.")
            return None
        with open(file_path, 'r+') as file:
            menu = json.load(file)
            menu['items'] = [
                item for item in menu['items'] if item['name'] != item_name
            ]
            json.dump(menu, file, indent=4)
        print(f"Item '{item_name}' removed from menu '{name}'.")


SpecialOrder = namedtuple(
    'SpecialOrder', ['name', 'price', 'menu_items']
)

special_1 = SpecialOrder(
    "Tropical Party", 35.0, [
        Beverage("Pina Colada", 10.0, "Large"),
        Appetizer("Shrimp Cocktail", 12.0, "Spicy"),
        MainCourse("Grilled Salmon", 20.0, False),
        Dessert("Mango Mousse", 8.0, 400)
    ]
)

special_2 = SpecialOrder(
    "Vegetarian Delight", 30.0, [
        Beverage("Herbal Tea", 5.0, "Medium"),
        Appetizer("Stuffed Peppers", 10.0, "Savory"),
        MainCourse("Vegetable Stir Fry", 15.0, False),
        Dessert("Fruit Salad", 5.0, 200)
    ]
)

special_3 = SpecialOrder(
    "Meat Lover's Feast", 50.0, [
        Beverage("Red Wine", 15.0, "Large"),
        Appetizer("Meat Platter", 20.0, "Savory"),
        MainCourse("BBQ Ribs", 25.0, True),
        Dessert("Chocolate Fondue", 10.0, 600)
    ]
)

class PaymentMethod:
    def __init__(self):
        pass

    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")

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

class OrdersQueue:
    def __init__(self):
        self.orders = []

    def enqueue(self, item):
        self.orders.append(item)

    def dequeue(self):
        if self.is_empty():
            print("The orders queue is empty")
            return None
        else:
            return self.orders.pop(0)

    def is_empty(self):
        return len(self.orders) == 0
    
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

if __name__ == "__main__":
    order_1 = Order()
    order_1.add_item(Appetizer("Spring Rolls", 5.0, "Spicy"))
    order_1.add_item(MainCourse("Grilled Chicken", 12.0, True))
    order_1.add_item(Dessert("Chocolate Cake", 4.0, 350))
    order_1.add_item(Dessert("Red Velvet Cake", 2.0, 300))
    order_1.add_item(SideDish("French Fries", 3.0, "Potato"))

    order_2 = Order()
    order_2.add_item(Beverage("Lemonade", 2.5, "Large"))
    order_2.add_item(MainCourse("Steak", 20.0, False))
    order_2.add_item(Dessert("Cheesecake", 6.0, 600))

    order_3 = Order()
    order_3.add_item(Beverage("Cola", 2.0, "Medium"))
    order_3.add_item(Appetizer("Nachos", 7.0, "Salty"))
    order_3.add_item(MainCourse("Fish & Chips", 15.0, True))
    order_3.add_item(Dessert("Ice Cream", 3.0, 200))
    order_3.add_item(SideDish("Salad", 4.0, "Vegetable"))

    orders_queue = OrdersQueue()
    orders_queue.enqueue(order_1)
    orders_queue.enqueue(order_2)
    orders_queue.enqueue(order_3)

    order_number = 1
    while not orders_queue.is_empty():
        current_order = orders_queue.dequeue()
        if current_order is not None:
            print(f"\nProcessing Order #{order_number}:")
            print(current_order.__str__())
            n_b, n_a, n_m, n_d, n_s = current_order.count_items()
            print(f"Beverages: {n_b}")
            print(f"Appetizers: {n_a}")
            print(f"Main Courses: {n_m}")
            print(f"Desserts: {n_d}")
            print(f"Side Dishes: {n_s}")
            if current_order.menu_items == special_1.menu_items:
                print("Special order: Tropical Party")
                print(f"Total bill amount: ${special_1.price:.2f}")
            elif current_order.menu_items == special_2.menu_items:
                print("Special order: Vegetarian Delight")
                print(f"Total bill amount: ${special_2.price:.2f}")
            elif current_order.menu_items == special_3.menu_items:
                print("Special order: Meat Lover's Feast")
                print(f"Total bill amount: ${special_3.price:.2f}")
            else:
                total = current_order.calculate_total_bill()
                print(f"Total bill amount: ${total:.2f}")
            order_number += 1