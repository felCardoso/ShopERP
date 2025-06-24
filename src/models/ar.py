from utils.core import CURRENCY


class AR:
    def __init__(
        self,
        sale_id,
        client_id,
        amount,
        due_date,
        payment_date=None,
        status="Pending",
        id=None,
    ):
        self.id = id
        self.sale_id = sale_id
        self.client_id = client_id
        self.amount = amount
        self.due_date = due_date
        self.payment_date = payment_date
        self.status = status

    def __repr__(self):
        return f"<AR ID: {self.id}[{self.status}] Sale ID: {self.sale_id} - {CURRENCY}{self.document}>"

    def to_dict(self):
        return {
            "id": self.id,
            "supplier_id": self.supplier_id,
            "client_id": self.client_id,
            "amount": self.amount,
            "due_date": self.due_date,
            "payment_date": self.payment_date,
            "status": self.status,
        }
