class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # invariant is max number of same character in the window

        char_counts = defaultdict(int)
        LEN = len(s)
        start, end = 0, 0
        max_window_size = 0
        max_freq = 0

        while end < LEN:
            char = s[end]
            char_counts[char] += 1

            max_freq = max(max_freq, char_counts[char])
            window_size = end - start + 1

            # print(start, end, s[start: end+1], max_freq, window_size)
            if max_freq + k >= window_size:
                max_window_size = max(max_window_size, window_size)
                end += 1
            else:
                char_counts[s[start]] -= 1
                start += 1
                end += 1

            
        
        return max_window_size