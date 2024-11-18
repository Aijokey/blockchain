import datetime
import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(data="Genesis Block", previous_hash="0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

def print_blocks(chain):
    for block in chain:
        print("Block--------------------")
        print("Timestamp:  ", block.timestamp)
        print("Data:       ", block.data)
        print("Hash:       ", block.hash)
        print("Previous Hash:  ", block.previous_hash)

blockchain = Blockchain()

blockchain.add_block(Block("First transaction", blockchain.get_latest_block().hash))
blockchain.add_block(Block("Second transaction", blockchain.get_latest_block().hash))

print("Is blockchain valid?", blockchain.is_chain_valid())

print_blocks(blockchain.chain)