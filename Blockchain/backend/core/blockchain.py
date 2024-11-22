import sys
sys.path.append("c:\\Users\\orangutanXwindows\\Documents\\DEV2\\Shockchain")

from Blockchain.backend.core.block import Block 
from Blockchain.backend.core.blockheader import BlockHeader 
from Blockchain.backend.util.util import sha256
import time

ZERO_HASH = "0" * 64
VERSION = 1


class Blockchain:
    def __init__(self):
        self.chain = []
        self.GenesisBlock()
        
    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)
       
        
    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp =int(time.time())
        Transaction = f"Trump is {BlockHeight} Prez bitcoin is at 99,000"
        merkleRoot = sha256(Transaction.encode()).hex()
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits) 
        blockheader.mine()
        self.chain.append(Block(BlockHeight, 1, blockheader.__dic__, 1, Transaction).__dic__)
        print(blockchain)
       
    def main(self):
        while True:
            lastBlock = self.chain[::-1]
            BlockHeight = lastBlock[0]["Height"] + 1
            prevBlockHash = lastBlock[0]['BlockHeader']['blockHash']
            self.addBlock(BlockHeight, prevBlockHash)
        
        
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.main()
    print(main)