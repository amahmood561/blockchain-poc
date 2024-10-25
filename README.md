# Simple Blockchain in Python

This project is a basic implementation of a blockchain using Python. It demonstrates core blockchain concepts such as blocks, proof of work, and chain validation. This blockchain is designed for educational purposes to provide an understanding of how blockchain technology works at a fundamental level.

## Features

- **Blockchain Structure**: Each block contains an index, timestamp, transactions, hash, previous block's hash, and a nonce.
- **Proof of Work (PoW)**: Each block must meet a simple proof-of-work condition before being added to the chain.
- **Genesis Block**: The first block in the chain.
- **Blockchain Integrity Check**: Ensures that the blockchain remains consistent and unaltered.

## Requirements

- Python 3.x

## Getting Started

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/simple-python-blockchain.git
   cd simple-python-blockchain
   ```

2. **Run the blockchain code**:
   Run the code directly using Python:
   ```bash
   python blockchain.py
   ```

## Code Overview

### Classes

- **`Block`**: Represents a single block in the blockchain.
  - Attributes: `index`, `previous_hash`, `transactions`, `timestamp`, `nonce`, `hash`.
  - Methods:
    - `compute_hash()`: Computes the hash of the block’s data.
  
- **`Blockchain`**: Manages the chain of blocks.
  - Attributes: `chain`, `difficulty`.
  - Methods:
    - `create_genesis_block()`: Creates the first block (Genesis Block) in the blockchain.
    - `get_last_block()`: Returns the last block in the chain.
    - `proof_of_work()`: Implements the PoW algorithm to validate blocks.
    - `add_new_block()`: Adds a new block with given transactions to the blockchain.
    - `is_chain_valid()`: Validates the integrity of the blockchain.

### Example Usage

```python
blockchain = Blockchain()
print("Genesis block added:", blockchain.chain[0])

# Adding new blocks with transactions
transactions = [{"sender": "Alice", "receiver": "Bob", "amount": 50}]
blockchain.add_new_block(transactions)
print("New block added:", blockchain.chain[-1])

transactions = [{"sender": "Bob", "receiver": "Charlie", "amount": 25}]
blockchain.add_new_block(transactions)
print("New block added:", blockchain.chain[-1])

# Check if the blockchain is valid
print("Blockchain valid?", blockchain.is_chain_valid())
```

## How It Works

1. **Genesis Block**: The blockchain begins with a single Genesis Block, which has a fixed previous hash.
2. **Adding Blocks**: New blocks are mined using the `proof_of_work` function, which requires the block’s hash to start with a certain number of zeros (based on the difficulty level).
3. **Blockchain Validation**: The `is_chain_valid()` function checks that each block's hash and previous hash are consistent, ensuring the chain's integrity.

