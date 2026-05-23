from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_terminal = False

class WordDictionary:
    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            curr = curr.children[ch]
        
        curr.is_terminal = True


    def search(self, word: str) -> bool:
        
        def dfs(node, pos):
            if pos == len(word):
                return node.is_terminal

            ch = word[pos]

            if ch == '.':
                return any(dfs(child, pos + 1) for child in node.children.values())

            
            if ch in node.children:
                return dfs(node.children[ch], pos + 1)
            
            return False
        
        return dfs(self.root, 0)


            
                
        




        
