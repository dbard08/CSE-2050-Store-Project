class cart:

  def __init__(self) -> None:
    self.items: list = []

  def add_product(self, product) -> None:
    self.items.append(product)

  def remove_product(self, product_id: str) -> bool:
    for index, item in enumerate(self.items):
      if item.get_id() == product_id:
        self.items.pop(index)
        return True
    return False

  def get_items(self) -> list:
    return self.items

  def calculate_total(self) -> float:
    return float(sum(item.get_price() for item in self.items))

  def is_empty(self) -> bool:
    return len(self.items) == 0
