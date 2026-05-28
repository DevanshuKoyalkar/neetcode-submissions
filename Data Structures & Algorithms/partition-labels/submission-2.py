class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # start and end of each letter 
        last_pos = {}

        for pos, ch in enumerate(s):
            last_pos[ch] = pos
        
        print(last_pos)
        
        start, end = 0, last_pos[s[0]]

        result = []
        count = 5
        while start < len(s):
            pos = start
            end = last_pos[s[start]]
            while pos <= end:
                end = max(end, last_pos[s[pos]])
                pos += 1
            result.append(end - start + 1)
            start = end + 1
        
        return result
