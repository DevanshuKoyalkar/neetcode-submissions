class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_char_count = defaultdict(int)
        
        LEN1, LEN2 = len(s1), len(s2)

        if LEN2 < LEN1: return False

        for ch in s1:
            target_char_count[ch] += 1
        candidate_char_count = defaultdict(int)

        # window of a fixed length which has to be moved
        for i in range(LEN1):
            candidate_char_count[s2[i]] += 1
        
        if candidate_char_count == target_char_count:
            return True
        start, end = 0, LEN1

        while end < LEN2:
            candidate_char_count[s2[end]] += 1
            candidate_char_count[s2[start]] -= 1

            is_match = True
            for ch in target_char_count:
                is_match &= (target_char_count[ch] == candidate_char_count[ch])
            
            if is_match:
                return True

            start += 1
            end += 1
        
        return False
        





