import datetime as date
import snakecoin

def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(1, date.datetime.now(), "Genesis Block", "0")
