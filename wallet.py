from crypto import generate_keys, sign_transaction, verify_signature

class Wallet:
    def __init__(self):
        self.public_key, self.private_key = generate_keys()

    def sign_transaction(self, transaction):
        return sign_transaction(self.private_key, transaction)

    def verify_transaction(self, transaction, signature):
        return verify_signature(self.public_key, transaction, signature)

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def to_string(self):
        return f"{self.sender}{self.receiver}{self.amount}"
