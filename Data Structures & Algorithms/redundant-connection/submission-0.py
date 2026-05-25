class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)

        parent = [i for i in range(n+1)]
        
        def findParent(node):
            if parent[node] == node:
                return node
            
            parent[node] = findParent(parent[node])
            return parent[node]

        for a, b in edges:
            parent_a = findParent(a)
            parent_b = findParent(b)

            if parent_a == parent_b:
                return [a,b]
            
            parent[parent_b] = a
        
        return [-1,-1]