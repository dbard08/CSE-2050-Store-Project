class store:

  def __init__(self) -> None:
    self.products: list = []
    self.customers: list = []

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
