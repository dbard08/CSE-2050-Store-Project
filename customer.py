from cart import ShoppingCart

class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id = str(customer_id)
        self.name = str(name)
        self.cart = ShoppingCart()

    def get_id(self) -> str:
        return self.customer_id

    def get_name(self) -> str:
        return self.name

    def get_cart(self) -> ShoppingCart:
        return self.cart

customer = Customer
