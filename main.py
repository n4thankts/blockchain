# Simple project that showcases how blockhain works and how transaction hashes are produced
#This is based on what I learned from Ivan on Tech Academy


#import the function that we made that's in the Block.py file
from Block import Block


blockchain = []

#create the first block
genesis_block = Block("Chancellor on the brink...", ["Nathan sent 1 BTC to John",
                                                      "George sent 2 BTC to Helen",
                                                      "Stefan sent 5 BTC to Raymond"])

#create the second block
second_block = Block(genesis_block.block_hash, ["John sent 4 BTC to Maria",
                                                "Nathan sent 2 BTC to George"])

#create the third block
third_block = Block(second_block.block_hash, ["Nathan sent 8 BTC to Matt",
                                              "Satoshi sent 7 BTC to George",])

#print the hash for each block using a print function
print("Block hash of the Genesis Block is:")
print(genesis_block.block_hash)

print("Block hash for the Second Block is:")
print(second_block.block_hash)

print("Block hash for the Third Block is:")
print(third_block.block_hash)

#Blockchain works like a puzzle. Each block has an influence in the next one. If you change even one letter
#from the transactions of the block, the block's hash and all the hashes after that block will change.
#It's like a book that every page page contains the last period from the previous page and uses it as a first period.
#It works exactly like a chain. That's why it's called Blockchain. 