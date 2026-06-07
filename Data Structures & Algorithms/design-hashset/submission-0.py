class MyHashSet:

    def __init__(self):
        self.val = 0
        

    def add(self, key: int) -> None:
        self.val = self.val | (1 << key)

    def remove(self, key: int) -> None:
        self.val = self.val & ~(1 << key)

    def contains(self, key: int) -> bool:
        if self.val & (1 << key):
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)