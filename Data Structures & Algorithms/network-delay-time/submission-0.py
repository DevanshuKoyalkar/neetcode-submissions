class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, start: int) -> int:
        distances = [float("inf")] * (n + 1)

        distances[start] = 0

        adj_list = defaultdict(list)

        for a, b, time in times:
            adj_list[a].append((b,time))

        
        # Priority queue stores tuples of (distance, node)
        pq = [(0, start)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            # Nodes can be added to the heap multiple times; skip if we found a shorter path already
            if current_distance > distances[current_node]:
                continue
            
            for neighbour, weight in adj_list[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    heapq.heappush(pq, (distance, neighbour))
        
        result = -1

        print(distances)
        for i in range(1, len(distances)):
            distance = distances[i]
            result = max(result, distance)
        
        return result if result != float("inf") else -1

