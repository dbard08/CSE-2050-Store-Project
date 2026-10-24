from order import Order
from order_queue import OrderQueue
from algorithms import selection_sort, insertion_sort, binary_search


class Store:
    def __init__(self) -> None:
        self.products: list = []
        self.customers: list = []
        self.orders: list = []
        self.order_queue = OrderQueue()
        self.order_history: list = []

    def add_product(self, product) -> bool:
        if self.find_product(product.get_id()) is not None:
            return False

        self.products.append(product)
        return True

    def find_product(self, product_id: str):
        for product in self.products:
            if product.get_id() == product_id:
                return product

        return None

    def add_customer(self, customer) -> bool:
        if self.find_customer(customer.get_id()) is not None:
            return False

        self.customers.append(customer)
        return True

    def find_customer(self, customer_id: str):
        for customer in self.customers:
            if customer.get_id() == customer_id:
                return customer

        return None

    def checkout(self, customer_id: str):
        customer = self.find_customer(customer_id)

        if customer is None:
            return None

        cart = customer.get_cart()

        if cart.is_empty():
            return None

        order_id = f"O{len(self.orders) + 1}"
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

    def get_orders(self) -> list:
        return self.orders

    def find_order(self, order_id: str):
        for order in self.orders:
            if order.get_id() == order_id:
                return order

        return None

    def get_order_history(self) -> list:
        return self.order_history

    def insertion_sort_products(self):
        """Sort stores products by ID using insertion sort"""
        insertion_sort(self.products)

    def selection_sort_products(self):
        """Sort stores products by ID using selection sort"""
        selection_sort(self.products)

    def binary_search_product(self, product_id):
        """Return the product with ID from the sorted list or none"""
        index = binary_search(self.products, product_id)
        if index == -1:
            return None
        return self.products[index]

    


store = Store
