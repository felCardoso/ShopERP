class Supplier:
    def __init__(self, name, document, address=None, phone=None, email=None, id=None):
        self.id = id
        self.name = name
        self.document = document
        self.address = address
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"<Supplier ID: {self.id}, Name: {self.name}, Document: {self.document}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "document": self.document,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
        }
