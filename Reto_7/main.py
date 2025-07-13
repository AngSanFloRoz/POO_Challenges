from package.menu_items.beverage import Beverage
from package.menu_items.appetizer import Appetizer
from package.menu_items.main_course import MainCourse
from package.menu_items.dessert import Dessert
from package.menu_items.side_dish import SideDish
from package.order import Order
from package.orders_queue import OrdersQueue
from package.specials import special_1, special_2, special_3


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