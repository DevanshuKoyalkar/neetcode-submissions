class Node:
    def __init__(self):
        self.ngbrs = {}
        self.is_terminal = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.ngbrs:
                curr.ngbrs[ch] = Node()
            
            curr = curr.ngbrs[ch]
        
        curr.is_terminal = True


    def search(self, word: str) -> bool:
        
        def dfs(node, pos):
            if pos == len(word):
                return node.is_terminal

            ch = word[pos]

            if ch != '.':
                if ch not in node.ngbrs:
                    return False
                return dfs(node.ngbrs[ch], pos + 1)
            
            for ngbr in node.ngbrs:
                if dfs(node.ngbrs[ngbr], pos + 1):
                    return True
            
            return False
        
        return dfs(self.root, 0)


            
                
        




        
