
class Node:
    def __init__(self):
        self.ngbrs = {}
        self.is_terminal = False
        
class PrefixTree:
    
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.ngbrs:
                curr.ngbrs[ch] = Node()

            curr = curr.ngbrs[ch]
                
        curr.is_terminal = True
        return


    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.ngbrs:
                return False
            curr = curr.ngbrs[ch]
        
        return curr.is_terminal
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.ngbrs:
                return False
            curr = curr.ngbrs[ch]
        
        return True
        