class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        start, end = 0, 0
        max_size = 0

        seen = {}
        while end < n:
            while end < n:
                ch = s[end]
                if ch not in seen or seen[ch] < start:
                    seen[s[end]] = end
                    max_size = max(max_size, end - start + 1) 
                    end += 1
                else:
                    start = seen[ch] + 1
                    break
            
        return max_size


