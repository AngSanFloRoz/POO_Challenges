import json
import os
from menu_item import MenuItem
from package.menu_items.beverage import Beverage
from package.menu_items.appetizer import Appetizer
from package.menu_items.main_course import MainCourse
from package.menu_items.dessert import Dessert
from package.menu_items.side_dish import SideDish

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
