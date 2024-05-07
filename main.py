### ATAR COMPUTER SCIENCE: Task 2 – Unit 3
## Papa Pizza Ordering System
## By Samuel Scott

import tkinter


# Rounding
def round_to(n, precision):
    correction = 0.5 if n >= 0 else -0.5
    return int(n / precision + correction) * precision


def round_to_05(n):
    return round_to(n, 0.05)


# Pizza topping and base customizations objects
# Classes contain attributes to help organise the pizza customization options
class customisation:
    class toppings:
        Light = "light"
        Normal = "normal"
        Extra = "extra"

    class pizza_base:
        Normal = "normal"
        Gluten_Free = "gluten_free"


# Parent pizza object
class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 1

        self.toppings_amount = customisation.toppings.Normal
        self.pizza_base = customisation.pizza_base.Normal

    def set_toppings_amount(self, value):
        self.toppings_amount = value

    def set_pizza_base(self, value):
        self.pizza_base = value

    def set_item_quantity(self, value):
        self.quantity = value


# Different types of pizzas
class Pepperoni(Pizza):
    def __init__(self):
        Pizza.__init__(self, name="Pepperoni", price=21.00)


class ChickenSupreme(Pizza):
    def __init__(self):
        Pizza.__init__(self, name="Chicken Supreme", price=23.50)


class BBQMeatlovers(Pizza):
    def __init__(self):
        Pizza.__init__(self, name="BBQ Meatlovers", price=25.50)


class VegSupreme(Pizza):
    def __init__(self):
        Pizza.__init__(self, name="Pepperoni", price=22.50)


class Hawaiian(Pizza):
    def __init__(self):
        Pizza.__init__(self, name="Pepperoni", price=19.00)


class Margherita(Pizza):
    def __init__(self):
        Pizza.__init__(self, name="Pepperoni", price=18.50)


class Sale:
    def __init__(self, _order):
        self._order = _order
        self.total_price = 0

    def calculate_price(self, discounted):
        sale_summary = {"total_price": 0, "discount_received": 0, "gst_amount": 0, "subtotal_price": 0}
        self.get_total_sale_price()
        price = self.total_price
        sale_summary["subtotal_price"] = self.total_price
        total_price = self.total_price

        if discounted:
            discount = self.calculate_discount()
            discount = round_to_05(discount)
            sale_summary["discount_received"] = discount
            total_price -= discount

        gst_amount = self.calculate_gst()

        sale_summary["gst_amount"] = discount

        total_price += gst_amount

        sale_summary["total_price"] = total_price

        return sale_summary

    def get_total_sale_price(self):
        for item in self._order.items.values():
            self.total_price += item.price

    def calculate_gst(self):
        # Calculate GST and round it to the nearest 5 cents
        gst = self.total_price * 0.1
        gst = round_to_05(gst)
        return gst

    def calculate_discount(self):
        # Calculate discount and round it to the nearest 5 cents
        discount = self.total_price * 0.05
        discount = round_to_05(discount)
        return discount


class DailySales(Sale):
    def __init__(self):
        Sale.__init__(self)


class Order:
    def __init__(self):
        self.customer_name = ""

        self.items = {}

    def set_customer_name(self, name):
        self.customer_name = name

    def add_item(self, item: Pizza):
        # Initialize item
        item = item()
        # Assigns each item with an item id; the item id is the position
        # of the which the item is inserted into the dictionary.
        item_id = 1 + len(self.items)
        self.items[item_id] = item
        return item_id

    def set_item_quantity(self, item_id, quantity):
        self.items[item_id].set_pizza_quantity(quantity)

    def list_items(self):
        formatted_items = ""
        for item in self.items.keys():
            formatted_items += f"item_id: {item}, item: {self.items[item].name} pizza, price: {self.items[item].price} quantity: {self.items[item].quantity}\n"
        return formatted_items


class MainApplication(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title("Papa Pizza Ordering System")

        self.mainloop()


def main():
    # app = MainApplication()
    order = Order()

    order.add_item(Margherita)
    order.add_item(Pepperoni)

    print(order.list_items())

    sale = Sale(order)

    print(sale.calculate_price(True))


if __name__ == "__main__":
    main()
