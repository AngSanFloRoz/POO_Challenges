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