### ATAR COMPUTER SCIENCE: Task 2 – Unit 3
## Papa Pizza Ordering System
## By Samuel Scott


# Rounding
def round_to(n, precision):
    correction = 0.5 if n >= 0 else -0.5
    return int(n / precision + correction) * precision


def round_to_05(n):
    return round_to(n, 0.05)


# Parent pizza object
class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 1

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

    def calculate_price(self, discounted, delivery):
        sale_summary = {"total_price": 0, "discount_received": 0, "gst_amount": 0, "subtotal_price": 0, "delivery": 0}
        self.get_total_sale_price()
        discount = 0
        sale_summary["subtotal_price"] = self.total_price
        total_price = self.total_price

        if discounted or total_price > 100:
            print("Applying 5% discount")
            discount = self.calculate_discount()
            discount = round_to_05(discount)
            sale_summary["discount_received"] = discount
            total_price -= discount

        if delivery:
            total_price += 8
            sale_summary["delivery"] = 8

        gst_amount = self.calculate_gst()

        sale_summary["gst_amount"] = gst_amount

        total_price += gst_amount

        sale_summary["total_price"] = total_price

        return sale_summary

    def get_total_sale_price(self):
        for item in self._order.items.values():
            self.total_price += (item.price * item.quantity)

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


class Order:
    def __init__(self):
        self.customer_name = ""

        self.items = {}

    def set_customer_name(self, name):
        self.customer_name = name

    def add_item(self, item: Pizza):
        # Assigns each item with an item id; the item id is the position
        # of the which the item is inserted into the dictionary.
        item_id = 1 + len(self.items)
        self.items[item_id] = item
        return item_id

    def set_item_quantity(self, item_id, quantity):
        if not item_id in self.items:
            print("Item doesn't exist")
            return
        self.items[item_id].set_item_quantity(quantity)

    def del_item(self, item_id):
        if not item_id in self.items:
            print("Item doesn't exist")
            return
        self.items.pop(item_id)

    def list_items(self):
        formatted_items = ""
        for item in self.items.keys():
            formatted_items += f"item_id: {item}, item: {self.items[item].name} pizza, price: {self.items[item].price} quantity: {self.items[item].quantity}\n"
        return formatted_items


pizzas_available = {
    "pepperoni": Pepperoni,
    "chicken": ChickenSupreme,
    "bbqmeat": BBQMeatlovers,
    "vegsupreme": VegSupreme,
    "hawaiian": Hawaiian,
    "margherita": Margherita
}


def main():
    # Initialize order
    order = None
    daily_sales = 0

    running = True

    while running:
        print(
            f"---Pizza Ordering System---\n"
            f"Daily Sales: ${daily_sales}\n"
            "1. Start a new order\n"
            "2. quit application\n"
        )

        main_option = input("Option: ")

        if main_option == "2":
            running = False
            continue

        elif main_option == "1":
            print("--////--\nNew order started!\n")
            order = Order()
            processed = False

            while not processed:
                # Figuring out what pizzas they want and adding it to the objects
                print(order.list_items())
                print(
                    "1. Add pizza\n"
                    "2. Change quantity of pizza\n"
                    "3. Delete pizza\n"
                    "4. Process Order\n"
                    "5. Delete order and go back to main menu\n"
                )

                option = input("Option: ")

                if option == "4":
                    # Processing order option
                    print("Are you sure you would like to process this order? (y/n)")

                    process_option = ""

                    while not process_option == "n":
                        process_option = input("Please type 'y' for yes and 'n' for no: ").lower()

                        if process_option == "y":
                            print("Processing order")
                            processed = True
                            break
                    continue

                elif option == "5":
                    # Deleting order option
                    print("Are you sure you would like to delete this order? (y/n)")

                    delete_option = ""

                    while not delete_option == "n":
                        delete_option = input("Please type 'y' for yes and 'n' for no: ").lower()

                        if delete_option == "y":
                            print("Deleted order")
                            processed = True
                            order = None
                            break
                    continue

                elif option == "1":
                    # Adding pizza option
                    pizzas_available_string = "\n---Pizza available---\nUse keyword in bracket to add that pizza.\n"
                    for pizza_keyword in pizzas_available.keys():
                        # Initialize object to get pizza name and price
                        pizza = pizzas_available[pizza_keyword]()
                        pizzas_available_string += f"{pizza.name} ({pizza_keyword}) - {pizza.price}\n"
                    print(pizzas_available_string)

                    pizza_option = ""

                    while not pizza_option in pizzas_available.keys():
                        pizza_option = input("Pizza option (type `cancel` to cancel adding pizza): ").lower()
                        if pizza_option == "cancel":
                            print("Adding pizza cancelled")
                            break

                    if not pizza_option:
                        continue

                    quantity_amount = None

                    while not quantity_amount:
                        try:
                            if quantity_amount == 0:
                                print("Cannot set quantity to 0")
                            quantity_amount = int(input("Quantity: "))
                        except ValueError:
                            # Ensure value is an interger
                            print("Must be an interger")

                    # Initialize to get pizza name and price and add it to the order
                    pizza = pizzas_available[pizza_option]()
                    pizza.set_item_quantity(quantity_amount)
                    order.add_item(pizza)
                    print(f"Adding {pizza.name} - {pizza.price}")

                elif option == "2":
                    # Set quantity from item id
                    item_id = None

                    while not item_id:
                        try:
                            item_id = int(input("Item ID: "))
                        except ValueError:
                            # Ensure value is an interger
                            print("Must be an interger")

                    quantity_amount = None

                    while not quantity_amount:
                        try:
                            quantity_amount = int(input("Quantity: "))
                        except ValueError:
                            # Ensure value is an interger
                            print("Must be an interger")

                    pizza = order.items[item_id]
                    print(f"Changed {pizza.name} quantity to {quantity_amount}, item_id: {item_id}")

                    order.set_item_quantity(item_id, quantity_amount)

                elif option == "3":
                    # Delete pizza from item id
                    item_id = None

                    while not item_id:
                        try:
                            item_id = int(input("Item ID: "))
                        except ValueError:
                            # Ensure value is an interger
                            print("Must be an interger")

                    pizza = order.items[item_id]
                    print(f"Deleted {pizza.name}, item_id: {item_id}")

                    order.del_item(item_id)

            # If the order was deleted continue to the main loop and main menu
            if not order:
                continue

            # Processing order and checkout

            sale = Sale(order)

            print("Do you have a membership with us: ")

            membership = False

            has_membership = ""

            while not has_membership == "n":
                has_membership = input("Please type 'y' for yes and 'n' for no: ").lower()

                if has_membership == "y":
                    membership = True
                    break

            print("Is this order being delivered: ")

            _delivery = False

            is_delivery = ""

            while not is_delivery == "n":
                is_delivery = input("Please type 'y' for yes and 'n' for no: ").lower()

                if is_delivery == "y":
                    _delivery = True
                    break

            sale_summary = sale.calculate_price(discounted=membership, delivery=_delivery)

            print(f"Sale Summary: {sale_summary}")

            daily_sales += sale_summary["total_price"]

        else:
            print("Please enter a valid option.\n")
            continue

    print("Thanks for using our Pizza Ordering System")


if __name__ == "__main__":
    main()
