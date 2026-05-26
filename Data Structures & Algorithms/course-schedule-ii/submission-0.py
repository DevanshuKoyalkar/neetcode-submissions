class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = defaultdict(list)

        for a, b in prerequisites:
            adj_list[b].append(a)
        
        result = []
        visited = set()

        def dfs(node, path):
            visited.add(node)
            path.append(node)
            for ngbr in adj_list[node]:
                if ngbr in path: # there is a backedge/circular dependency
                    return False
                
                if not dfs(ngbr, path.copy()):
                    return False
            
            path.pop()
            result.append(node)
            return True

        for node in range(numCourses):
            if node in visited:
                continue

            if not dfs(node, []):
                return []
        
        result.reverse()
        return result

