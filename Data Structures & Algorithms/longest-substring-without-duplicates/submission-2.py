class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        start, end = 0, 0
        max_size = 0

        seen = {}

        while end < n:
            ch = s[end]

            if ch in seen:
                start = max(start, seen[ch] + 1)
            seen[ch] = end
            
            max_size = max(max_size, end - start + 1)
            end += 1

        return max_size
            



