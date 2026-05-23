class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)
        for a, b in prerequisites:
            adj_list[b].append(a)

        visited = set()

        def dfs(node, path):
            path.append(node)
            visited.add(node)

            for ngbr in adj_list[node]:
                if ngbr in path:
                    return False
                
                if not dfs(ngbr, path):
                    return False


            path.pop()
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i, []):
                    return False
        
        return True
            
