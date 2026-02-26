class FoodItem:
    def __init__(self, name, price, prep_time):
        self.name = name
        self.price = price
        self.prep_time = prep_time


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        return sum(item.price for item in self.items)

    def total_prep_time(self):
        if not self.items:
            return 0
        return max(self.items, key=lambda item: item.prep_time).prep_time


class Bill:
    def __init__(self, order):
        self.order = order

    def bill_amount(self):
        return self.order.total_price()


# Creating food items
burger = FoodItem("Burger", 150, 10)
pizza = FoodItem("Pizza", 300, 20)
coke = FoodItem("Coke", 50, 2)

# Creating order
order1 = Order()
order1.add_item(burger)
order1.add_item(pizza)
order1.add_item(coke)

# Creating bill
bill1 = Bill(order1)

print("Total Price:", bill1.bill_amount())
print("Total Preparation Time:", order1.total_prep_time())