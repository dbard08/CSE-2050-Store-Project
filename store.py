from order import Order
from order_queue import OrderQueue
from algorithms import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    binary_search,
    recursive_total_price,
    fewest_coins,
)


class Store:
    def __init__(self):
        self.products = []
        self.customers = []
        self.orders = []
        self.order_queue = OrderQueue()
        self.order_history = []

    def add_product(self, product):
        if self.find_product(product.get_id()) is not None:
            return False

        self.products.append(product)
        return True

    def find_product(self, product_id):
        for product in self.products:
            if product.get_id() == product_id:
                return product

        return None

    def add_customer(self, customer):
        if self.find_customer(customer.get_id()) is not None:
            return False

        self.customers.append(customer)
        return True

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.get_id() == customer_id:
                return customer

        return None

    def checkout(self, customer_id):
        customer = self.find_customer(customer_id)

        if customer is None:
            return None

        cart = customer.get_cart()

        if cart.is_empty():
            return None

        order_id = "O" + str(len(self.orders) + 1)
        order = Order(order_id, customer, cart.get_items())

        self.orders.append(order)
        self.order_queue.enqueue(order)
        cart.items.clear()

        return order

    def process_next_order(self):
        order = self.order_queue.dequeue()

        if order is None:
            return None

        order.set_status("PROCESSING")
        self.order_history.insert(0, order)

        return order

    def get_orders(self):
        return self.orders

    def find_order(self, order_id):
        for order in self.orders:
            if order.get_id() == order_id:
                return order

        return None

    def get_order_history(self):
        return self.order_history

    def bubble_sort_products(self):
        bubble_sort(self.products)

    def selection_sort_products(self):
        selection_sort(self.products)

    def insertion_sort_products(self):
        insertion_sort(self.products)

    def binary_search_product(self, product_id):
        index = binary_search(self.products, product_id)
        if index == -1:
            return None
        return self.products[index]

    def recursive_catalog_total(self):
        return recursive_total_price(self.products)

    def calculate_change(self, coins, amount):
        return fewest_coins(coins, amount)


store = Store
