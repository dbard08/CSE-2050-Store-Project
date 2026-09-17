from product import Product

class Cart:
    def __init__(self) -> None:
        self.items: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.items.append(product)

    def remove_product(self, product_id: str) -> bool:
        for index, item in enumerate(self.items):
            if item.get_id() == product_id:
                self.items.pop(index)
                return True
        return False

    def get_items(self) -> list[Product]:
        return self.items

    def calculate_total(self) -> float:
        return round(sum(item.get_price() for item in self.items), 2)

    def is_empty(self) -> bool:
        return len(self.items) == 0
