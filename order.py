class Order:
    def __init__(self, order_id: str, customer, items: list):
        self.order_id = order_id
        self.customer = customer
        self.items = list(items)
        self.status = "PENDING"

    def get_id(self) -> str:
        return self.order_id

    def get_customer(self):
        return self.customer

    def get_items(self) -> list:
        return self.items

    def get_status(self) -> str:
        return self.status

    def set_status(self, status: str) -> None:
        self.status = status

    def calculate_total(self) -> float:
        return sum(product.get_price() for product in self.items)
