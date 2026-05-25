class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(cand):
            return cand == cand[::-1]
        
        LEN = len(s)
        if not LEN:
            return [[]]
        
        if LEN == 1:
            return [[s]]
        
        result = []
        for i in range(1, LEN + 1):
            if not is_palindrome(s[:i]):
                continue
            
            
            tail_partitions = self.partition(s[i:])
            # print(s, i, s[:i], s[i:], tail_partitions)

            for tail_partition in tail_partitions:
                result.append([s[:i]] + tail_partition)
        
        return result

