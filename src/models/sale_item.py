from utils.core import CURRENCY


class Sale_Item:
    def __init__(self, sale_id, product_id, quantity, unit_price, id=None):
        self.id = id
        self.sale_id = sale_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price

    def __repr__(self):
        return f"<Sale_Product ID: {self.id}, {self.quantity}x, [{CURRENCY}{self.unit_price}]>"

    def to_dict(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "date": self.date,
            "total": self.total,
            "status": self.status,
        }
