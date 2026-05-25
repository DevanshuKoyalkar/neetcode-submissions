class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)

        parent = [i for i in range(n + 1)]
        rank = [1 for _ in range(n + 1)]
        
        def findParent(node):
            if parent[node] == node:
                return node
            
            # path compression
            parent[node] = findParent(parent[node])
            return parent[node]

        for a, b in edges:
            parent_a = findParent(a)
            parent_b = findParent(b)

            if parent_a == parent_b:
                return [a,b]
            
            if rank[parent_a] >= rank[parent_b]:
                rank[parent_a] += rank[parent_b]
                parent[parent_b] = a
            else:
                rank[parent_b] += rank[parent_a]
                parent[parent_a] = b
        
        return [-1,-1]