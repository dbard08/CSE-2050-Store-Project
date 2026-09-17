class Product:
    def __init__(self, product_id: str, name: str, price: float) -> None:
        self.product_id = str(product_id)
        self.name = str(name)
        self.price = float(price)

    def get_id(self) -> str:
        return self.product_id

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

product = Product
