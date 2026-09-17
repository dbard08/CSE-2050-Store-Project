class customer:
    def __init__(self, customer_id:str, name:str):
        self.customer_id = customer_id
        self.name = name

    def get_id(self):
        return self.customer_id

    def get_name(self):
        return self.name


