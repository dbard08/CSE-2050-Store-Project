from cart import Cart

class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.cart = Cart()

    def get_id(self) -> str:
        return self.customer_id

    def get_name(self) -> str:
        return self.name

    def get_cart(self) -> Cart:
        return self.cart
