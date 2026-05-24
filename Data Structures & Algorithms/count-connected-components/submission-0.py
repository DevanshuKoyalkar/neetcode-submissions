class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = defaultdict(list)

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for ngbr in adj_list[node]:
                if ngbr == parent or ngbr in visited:
                    continue
                
                dfs(ngbr, node)
        
        counter = 0
        for i in range(n):
            if i not in visited:
                dfs(i,-1)
                counter += 1
        
        return counter