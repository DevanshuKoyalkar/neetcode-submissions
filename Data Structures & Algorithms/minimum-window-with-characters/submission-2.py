class Solution:
    def minWindow(self, s:str, t: str) -> str:
        if t == "": return ""

        s_count, t_count = defaultdict(int), defaultdict(int)
        have = 0
        
        for ch in t:
            t_count[ch] += 1

        need = len(t_count)
        min_len = 9999999
        result = tuple()
        

        end = start = 0

        while end < len(s):
            ch = s[end]
            s_count[ch] += 1
            

            if s_count[ch] == t_count[ch]:
                have += 1
            
            while have == need: # valid window we can start reducing
                # print(s[start: end + 1], min_len, result)
                if min_len > end - start + 1:
                    min_len = end - start + 1
                    result = (start, end)

                
                start_ch = s[start]
                s_count[start_ch] -= 1
                start += 1
                if s_count[start_ch] < t_count[start_ch]:
                    have -= 1
            end += 1
            
        if min_len == 9999999:
            return ""
        
        l, r = result
        return s[l: r+1]

                

            



    def minWindow2(self, s: str, t: str) -> str:
        target_char_counts = defaultdict(int)

        for ch in t:
            target_char_counts[ch] += 1
        
        LEN = len(s)
        start, end = 0, 0
        window_counts = defaultdict(int)

        min_valid_window = 1000
        result = ""

        def is_valid(char_counts):
            for ch in target_char_counts:
                if char_counts[ch] < target_char_counts[ch]:
                    return False
            
            return True

        while end < LEN:
            window_char_counts[s[end]] += 1

            while start <= end and is_valid(window_char_counts):
                if min_valid_window > end - start + 1:
                    min_valid_window = end - start + 1
                    result = s[start: end + 1]
                
                start_ch = s[start]
                window_char_counts[start_ch] -= 1
                start += 1

            end += 1
        
        return result
