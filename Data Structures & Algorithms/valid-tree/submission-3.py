class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = len(edges)

        if m != n-1:
            return False

        visited = set()

        adj_list = defaultdict(list)

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        # recursive
        def dfs_recursive(node, parent):
            visited.add(node)

            for ngbr in adj_list[node]:
                if ngbr == parent:
                    continue
                if ngbr in visited:
                    return False # back edge

                if not dfs(ngbr, node):
                    return False
            
            return True

        def dfs_stack(start, pre):
            visited.add(start)
            stack = [(start, pre)]

            while stack:
                node, parent = stack.pop()

                for ngbr in adj_list[node]:
                    if ngbr == parent: 
                        continue
                    if ngbr in visited:
                        return False
                    
                    visited.add(ngbr)
                    stack.append((ngbr, node))
            
            return True

        
        return dfs_stack(0,-1) and len(visited) == n
                
