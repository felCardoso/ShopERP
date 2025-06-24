from utils.core import CURRENCY


class AP:
    def __init__(
        self,
        supplier_id,
        description,
        amount,
        due_date,
        payment_date=None,
        status="Pending",
        id=None,
    ):
        self.id = id
        self.supplier_id = supplier_id
        self.description = description
        self.amount = amount
        self.due_date = due_date
        self.payment_date = payment_date
        self.status = status

    def __repr__(self):
        return f"<AP ID: {self.id}[{self.status}] Supplier ID: {self.supplier_id} - {CURRENCY}{self.document}>"

    def to_dict(self):
        return {
            "id": self.id,
            "supplier_id": self.supplier_id,
            "description": self.description,
            "amount": self.amount,
            "due_date": self.due_date,
            "payment_date": self.payment_date,
            "status": self.status,
        }
