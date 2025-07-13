from collections import namedtuple
from package.menu_items.beverage import Beverage
from package.menu_items.appetizer import Appetizer
from package.menu_items.main_course import MainCourse
from package.menu_items.dessert import Dessert

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
