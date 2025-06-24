from utils.core import CURRENCY


class Sale:
    def __init__(self, client_id, date, total, status="Completed", id=None):
        self.id = id
        self.client_id = client_id
        self.date = date
        self.total = total
        self.status = status

    def __repr__(self):
        return f"<Sale ID: {self.id}, Date: {self.name}, Total: {CURRENCY}{self.total}>"

    def to_dict(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "date": self.date,
            "total": self.total,
            "status": self.status,
        }
