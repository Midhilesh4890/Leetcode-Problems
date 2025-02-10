class Node:
    def __init__(self, key: int, value: int):
        # Initializes each node with a key, a value, and optionally pointers to previous and next nodes.
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # Initializes the LRUCache with a specific capacity.
        self.capacity = capacity
        self.cache = {}  # Dictionary to hold key-node pairs for O(1) access.
        # Dummy nodes to simplify edge cases in the doubly linked list.
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __add_node(self, node):
        # Helper function to add a node right after the head.
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def __remove_node(self, node):
        # Helper function to remove an existing node from the linked list.
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        # Returns the value of the node identified by `key`, and moves the node to the front of the list.
        if key not in self.cache:
            return -1  # Return -1 if key is not found.
        node = self.cache[key]
        self.__remove_node(node)  # Move the accessed node to the front.
        self.__add_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # Updates the value of the node with `key` if it exists, otherwise adds a new node.
        if key in self.cache:
            # Update the node and move it to the front.
            self.__remove_node(self.cache[key])
            self.cache[key].value = value
            self.__add_node(self.cache[key])
        else:
            # Add a new node if it does not exist.
            if len(self.cache) == self.capacity:
                # If the cache is at capacity, remove the least recently used item.
                lru = self.tail.prev
                self.__remove_node(lru)
                del self.cache[lru.key]
            # Create a new node and add it to the front.
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.__add_node(new_node)

# Example Usage
cache = LRUCache(2)

# Test put operations and LRU property
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       # Returns 1, cache = {1=1, 2=2}

cache.put(3, 3)           # Evicts key 2, cache = {1=1, 3=3}
print(cache.get(2))       # Returns -1 (not found)
print(cache.get(3))       # Returns 3, cache = {1=1, 3=3}

# Test update and get operations
cache.put(1, 10)          # Updates existing key 1, cache = {1=10, 3=3}
print(cache.get(1))       # Returns 10
print(cache.get(3))       # Returns 3
