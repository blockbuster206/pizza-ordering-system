### ATAR COMPUTER SCIENCE: Task 2 – Unit 3
## Papa Pizza Ordering System
## By Samuel Scott

# Pizza topping and base customizations objects
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

        self.toppings_amount = customisation.toppings.Normal
        self.pizza_base = customisation.pizza_base.Normal

    def set_toppings_amount(self, value):
        self.toppings_amount = value


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
    def __init__(self):
        self.total_amount = 0

    def add_amount(self):
        pass


class DailySales(Sale):
    def __init__(self):
        Sale.__init__(self)


class Order(Sale):
    def __init__(self):
        Sale.__init__(self)

        self.items = []


sales = {}


def main():
    pass


if __name__ == "__main__":
    main()
