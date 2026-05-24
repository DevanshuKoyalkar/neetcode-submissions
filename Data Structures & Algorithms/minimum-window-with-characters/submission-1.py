class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_char_counts = defaultdict(int)

        for ch in t:
            target_char_counts[ch] += 1
        
        LEN = len(s)
        start, end = 0, 0
        window_char_counts = defaultdict(int)

        min_valid_window = 1000
        result = ""

        def is_valid(char_counts):
            for ch in target_char_counts:
                if char_counts[ch] < target_char_counts[ch]:
                    return False
            
            return True

        while end < LEN:
            ch = s[end]
            window_char_counts[ch] += 1

            while start <= end and is_valid(window_char_counts):
                valid_window_len = end - start + 1
                if min_valid_window > valid_window_len:
                    min_valid_window = valid_window_len
                    result = s[start: end + 1]
                
                start_ch = s[start]
                window_char_counts[start_ch] -= 1
                start += 1

            end += 1
        
        return result
