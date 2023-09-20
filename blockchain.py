import hashlib
from time import gmtime, strftime

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class Block:
    def __init__(self, timestamp, data, index, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calc_hash()
    
    def _calc_hash(self):
        sha = hashlib.sha256()
        sha_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(sha_str.encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        repr_str  = 'block hash: {}'.format(self.hash)
        repr_str += '\nprevious hash: {}'.format(self.previous_hash)
        repr_str += '\ntimestamp: {}'.format(self.timestamp)
        repr_str += '\nblock data: {}'.format(self.data)
        return repr_str

class Blockchain:
    def __init__(self):
        self.head = Node(self._build_genesis_block())
        self.tail = self.head
        self.size = 1

    def add(self, block):
        if block.previous_hash != self.last_block.previous_hash:
            return

        node = Node(block)
        node.next = self.head
        self.head = node
        self.size += 1
        
    def get(self, index):
        if index < 0:
            return None

        current_node = self.head
        while current_node is not None:
            if current_node.value.index == index:
                break
            current_node.next = current_node
        
        return current_node.value

    def get_size(self):
        return self.size
    
    def _build_genesis_block(self):
        index = 0
        timestamp = strftime("%H:%M %m/%d/%Y", gmtime())
        data = "genesis"
        prev_hash = 0
        return Block(timestamp, data, index, prev_hash)
    
    @property
    def last_block(self):
        return self.head.value

    def __str__(self):
        indent = 7
        current_node = self.head
        s = ""
        while current_node is not None:
            s += str(current_node.value)
            if current_node.next is not None:
                s += ' ' * indent + '|\n'
                s += ' ' * indent + 'V\n'
            current_node = current_node.next
        return s

# Tests
chain = Blockchain()

# Test 1: expected size 1. Genesis block is there
print("Test 1")
print(chain)
print(f"Chain size: {chain.get_size()}")

# Test 2: expected size 4. 3 transaction bocks are there
print("Test 2")
block = Block(strftime("%H:%M %m/%d/%Y", gmtime()),
                        "transaction 1",
                        chain.last_block.index + 1,
                        chain.last_block.previous_hash)
chain.add(block)

block = Block(strftime("%H:%M %m/%d/%Y", gmtime()),
                        "transaction 2",
                        chain.last_block.index + 1,
                        chain.last_block.previous_hash)
chain.add(block)

block = Block(strftime("%H:%M %m/%d/%Y", gmtime()),
                        "transaction 3",
                        chain.last_block.index + 1,
                        chain.last_block.previous_hash)
chain.add(block)

print(chain)
print("Chain size: ", chain.get_size())

#Test 3: Expected: size 4. Block with "Transaction 4" wasn't added due to prev hash mismatch
print("Test 3")
block = Block(strftime("%H:%M %m/%d/%Y", gmtime()),
                        "transaction 4",
                        chain.last_block.index + 1,
                        "u9acd81a49c5ffe5c95c10a7c3793e70b784188bb3c02f7417b66f3fd732a56b")
chain.add(block)

print(chain)
print("Chain size: ", chain.get_size())

#Test 4: Expected: block with "Transaction 3"
print("Test 4")
print(chain.get(3))

