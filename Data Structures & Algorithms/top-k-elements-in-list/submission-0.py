class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)

        heap = []

        for num in num_count.keys():
            heapq.heappush(heap, (num_count[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
            

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res

