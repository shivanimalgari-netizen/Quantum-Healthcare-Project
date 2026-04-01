import hashlib
import time

blockchain = []

def create_block(data, previous_hash):
    block = {
        "timestamp": time.time(),
        "data": data,
        "previous_hash": previous_hash
    }
    block["hash"] = hashlib.sha256(str(block).encode()).hexdigest()
    return block

def add_to_blockchain(data_list):
    previous_hash = "0"

    for data in data_list:
        block = create_block(data, previous_hash)
        blockchain.append(block)
        previous_hash = block["hash"]

    return blockchain