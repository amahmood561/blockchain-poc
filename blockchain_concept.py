import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.transactions = transactions
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_data = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.nonce}"
        return hashlib.sha256(block_data.encode()).hexdigest()

    def __repr__(self):
        return f"Block({self.index}, {self.hash})"

class Blockchain:
    difficulty = 2  # number of leading zeros in the hash

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, block):
        block.previous_hash = self.get_last_block().hash
        block.hash = block.compute_hash()
        self.chain.append(block)

    def proof_of_work(self, block):
        while not block.hash.startswith("0" * Blockchain.difficulty):
            block.nonce += 1
            block.hash = block.compute_hash()
        return block.hash

    def add_new_block(self, transactions):
        new_block = Block(len(self.chain), self.get_last_block().hash, transactions)
        new_block.hash = self.proof_of_work(new_block)
        self.add_block(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check current block's hash
            if current_block.hash != current_block.compute_hash():
                return False
            # Check hash link between blocks
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Example usage
blockchain = Blockchain()
print("Genesis block added:", blockchain.chain[0])

# Adding new blocks
transactions = [{"sender": "Alice", "receiver": "Bob", "amount": 50}]
blockchain.add_new_block(transactions)
print("New block added:", blockchain.chain[-1])

transactions = [{"sender": "Bob", "receiver": "Charlie", "amount": 25}]
blockchain.add_new_block(transactions)
print("New block added:", blockchain.chain[-1])

# Check validity of the blockchain
print("Blockchain valid?", blockchain.is_chain_valid())
