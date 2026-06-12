class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # max frequency character in the window repeats a times
        # a + k >= window_len
        # a >= window_len - k
        start = 0
        n = len(s)
        end = 0

        window = defaultdict(int)
        max_window_size = 0


        while end < n:
            ch = s[end]

            window[ch] += 1
            window_size = end - start + 1

            max_freq = max(list(window.values()))

            while max_freq < window_size - k:
                window[s[start]] -= 1
                start += 1
                window_size = end - start + 1
                
            max_window_size = max(window_size, max_window_size)
            
            end += 1
        
        return max_window_size






        