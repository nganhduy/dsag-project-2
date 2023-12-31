class double_node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"
class double_linked_list:
    def __init__(self):
        self.head = double_node(None)
        self.tail = double_node(None)
        self.head.prev, self.head.next = None, self.tail
        self.tail.prev, self.tail.next = self.head, None
        self.num_of_nodes = 0  
    
    def append(self, value):
        doubleNode = double_node(value)
        prev_to_tail = self.tail.prev
        self.tail.prev = doubleNode
        doubleNode.next = self.tail
        doubleNode.prev = prev_to_tail
        prev_to_tail.next = doubleNode
        self.num_of_nodes += 1
        return doubleNode        

    def prepend(self, value):
        node = double_node(value)
        next_to_head = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_to_head
        next_to_head.prev = node
        self.num_of_nodes += 1
        return node

    def remove(self, node):
        if node == None or self.size() == 0:
            return

        prev_to_node = node.prev
        next_to_node = node.next
        prev_to_node.next = node.next
        next_to_node.prev = node.prev

        self.num_of_nodes -= 1

    def size(self):
        return self.num_of_nodes

    def __repr__(self):
        s = f"Head <->"
        node = self.head.next
        for _ in range(self.num_of_nodes):
            s += f" {node} <->"
            node = node.next
        s += f" Tail"

        return s
class LRU_Cache(object):
    def __init__(self, capacity = 10):
        # Initialize class variables
        self.map = dict()
        self.storage = double_linked_list()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.map:
            node = self.map[key]
            _, value = node.value
            if node != self.storage.head.next:
                self.storage.remove(node)
                self.map[key] = self.storage.prepend((key, value))
            return value

        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.map:
            if self.is_full():
                # if at capacity, remove the oldest item and the key
                oldest = self.storage.tail.prev
                self.storage.remove(oldest)
                key_of_oldest, _ = oldest.value
                self.map.pop(key_of_oldest)
        else:
            self.storage.remove(self.map[key])
        self.map[key] = self.storage.prepend((key, value))

    def is_full(self):
        return self.storage.size() == self.capacity

    def __repr__(self):
        s = f"map  => {{"
        for k, v in self.map.items():
            s += f"{k}: {v}, "
        s += "}"
        s += f"\nlist => {self.storage}"
        return s


# Tests
our_cache = LRU_Cache(5)

value = our_cache.get(6)     # returns -1
print(value)                

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

# Test case 2: get the same value 5 times

value = our_cache.get(4)      # returns 1
print(value)
value = our_cache.get(4)      # returns 1
print(value)
value = our_cache.get(4)      # returns 1
print(value)
value = our_cache.get(4)      # returns 1
print(value)
value = our_cache.get(4)      # returns 1
print(value)

# Test case 3

value = our_cache.get(2)      # returns 2
print(value)

# Test case 4

value = our_cache.get(9)      # returns -1 because 9 is not present in the cache
print(value)

# Test case 5

our_cache.set(5, 5)
our_cache.set(6, 6)
value = our_cache.get(3)      # returns -1 because the cache reached it's capacity and 1 was the least recently used entry
print(value)

# Test case 6

our_cache.set(2, 10)          # check that we replace the value in case the key is already there
value = our_cache.get(2)      # returns 10
print(value)

# Test case 7

value = our_cache.get(4)      # returns 4 (check that previous get didn't pop the least recent but only replaced)
print(value)