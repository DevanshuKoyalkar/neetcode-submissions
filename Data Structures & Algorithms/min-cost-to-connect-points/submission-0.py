class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = [] # tuples of (weight, x, y)

        V = len(points)

        for i in range(V):
            for j in range(i):
                x1, y1 = points[i]
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)

                edges.append((dist, (x1, y1), (x2, y2)))
        
        edges.sort(key = lambda x: x[0]) # based on distance

        parent = [i for i in range(V)]
        idx = {}
        for i, point in enumerate(points):
            idx[tuple(point)] = i

        def getParent(i):
            if parent[i] == i:
                return i
            
            parent[i] = getParent(parent[i])
            return parent[i]

        result = 0
        # print(edges)
        for edge in edges:
            dist, point1, point2 = edge
            idx1, idx2 = idx[point1], idx[point2]

            parent1, parent2 = getParent(idx1), getParent(idx2)
            
            if parent1 != parent2:
                # print(dist, point1, point2, parent)
                result += dist
                parent[parent2] = parent1
        
        return result




            