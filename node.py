from blockchain import Blockchain, Block
from wallet.py import Wallet, Transaction

class Node:
    def __init__(self):
        self.blockchain = Blockchain()
        self.wallet = Wallet()
        self.pending_transactions = []

    def create_transaction(self, receiver, amount):
        transaction = Transaction(self.wallet.public_key, receiver, amount)
        signature = self.wallet.sign_transaction(transaction.to_string())
        self.pending_transactions.append((transaction, signature))

    def mine_pending_transactions(self):
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, int(time.time()), self.pending_transactions)
        self.blockchain.add_block(new_block)
        self.pending_transactions = []

    def is_chain_valid(self):
        return self.blockchain.is_chain_valid()
