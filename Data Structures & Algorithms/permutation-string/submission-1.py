class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        LEN1, LEN2 = len(s1), len(s2)

        if LEN2 < LEN1: return False

        s1_counts = [0] * 26
        window_counts = [0] * 26

        # window of a fixed length which has to be moved
        for i in range(LEN1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            window_counts[ord(s2[i]) - ord('a')] += 1
        
        if s1_counts == window_counts:
            return True
        start, end = 0, LEN1

        while end < LEN2:
            window_counts[ord(s2[end]) - ord('a')] += 1
            window_counts[ord(s2[start]) - ord('a')] -= 1

            if window_counts == s1_counts:
                return True

            start += 1
            end += 1
        
        return False
        





