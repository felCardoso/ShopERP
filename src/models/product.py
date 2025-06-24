from utils.core import CURRENCY


class Product:
    def __init__(self, name, price, stock=0, description=None, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"<Product ID: {self.id}, Name: {self.name}, Price: {CURRENCY}{self.price}, Stock: {self.stock}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
        }
