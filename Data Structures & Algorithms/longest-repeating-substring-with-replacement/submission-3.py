class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # invariant is max number of same character in the window

        char_counts = defaultdict(int)
        LEN = len(s)
        start, end = 0, 0
        max_window_size = 0
        max_freq = 0

        for end,char in enumerate(s):
            char_counts[char] += 1

            max_freq = max(max_freq, char_counts[char])
            window_size = end - start + 1

            if max_freq + k >= window_size:
                max_window_size = max(max_window_size, window_size)
            else:
                char_counts[s[start]] -= 1
                start += 1

            
        
        return max_window_size