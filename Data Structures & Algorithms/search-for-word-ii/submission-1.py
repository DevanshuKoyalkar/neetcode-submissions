
class TrieNode:
    def __init__(self):
        self.ngbrs = {}
        self.is_terminal = False
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, s):
        curr = self.root

        for ch in s:
            if ch not in curr.ngbrs:
                curr.ngbrs[ch] = TrieNode()
            
            curr = curr.ngbrs[ch]
        curr.is_terminal = True
        curr.word = s
    
    def get_root(self):
        return self.root

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_trie = Trie()

        # first build a trie and try to construct the trie at each node
        for word in words:
            word_trie.add(word)
        
        N, M = len(board), len(board[0])
        result = set()
        path = []

        def dfs(x, y, trie_node):
            path.append((x,y))

            trie_node = trie_node.ngbrs[board[x][y]]
            if trie_node.is_terminal:
                result.add(trie_node.word)

            
            for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                
                if (
                    0 <= nx < N and 
                    0 <= ny < M and
                    (nx, ny) not in path and 
                    board[nx][ny] in trie_node.ngbrs
                ):
                    dfs(nx, ny, trie_node)
            
            path.pop()
    
        for i in range(N):
            for j in range(M):
                if board[i][j] not in word_trie.get_root().ngbrs:
                    continue
                dfs(i,j, word_trie.get_root())
        
        return list(result)






