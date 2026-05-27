
class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self._remove(node)
        self._add_to_head(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self._remove(self.key_to_node[key])

        # completely create new node
        node = Node(key, value)

        self._add_to_head(node)
        self.key_to_node[key] = node

        if len(self.key_to_node) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            # print(key, value, lru_node.key, lru_node.val)
            # print(self.key_to_node.keys())
            del self.key_to_node[lru_node.key]
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_head(self, node):
        """Always inserts cleanly between the dummy head and the first real node."""
        first_node = self.head.next

        self.head.next = node
        node.prev = self.head
        first_node.prev = node
        node.next = first_node

        
