class product:
    def __init__(self, name:str, price: float, product_id: str):
        self.name = name
        self.price = price
        self.product_id = product_id

    def get_id(self):
        return self.product_id

    def get_name(self):
        return self.name

    def get_price(self):
        return f"${self.price:.2f}"



if __name__ == "__main__":
    p1 = product("Banana", 7.00, "BAN123")
    print(p1.get_id())
    print(p1.get_name())
    print(p1.get_price())

