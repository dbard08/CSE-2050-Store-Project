from product import Product
from customer import Customer

class Store:
    def __init__(self) -> None:
        self.products: list[Product] = []
        self.customers: list[Customer] = []

    def add_product(self, product: Product) -> bool:
        if self.find_product(product.get_id()) is not None:
            return False
        self.products.append(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_id() == product_id:
                return product
        return None

    def add_customer(self, customer: Customer) -> bool:
        if self.find_customer(customer.get_id()) is not None:
            return False
        self.customers.append(customer)
        return True

    def find_customer(self, customer_id: str) -> Customer | None:
        for customer in self.customers:
            if customer.get_id() == customer_id:
                return customer
        return None
