class Product:
    def __init__(self, name: str, price: float, product_id: str) -> None:
        self.name = name
        self.price = float(price)
        self.product_id = product_id

    def get_id(self) -> str:
        return self.product_id

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def get_formatted_price(self) -> str:
        return f"${self.price:.2f}"

    def __repr__(self) -> str:
        return f"Product(id='{self.product_id}', name='{self.name}', price={self.price:.2f})"
