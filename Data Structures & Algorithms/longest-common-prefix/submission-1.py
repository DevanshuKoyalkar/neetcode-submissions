class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def lcp(str1, str2):
            if len(str2) < len(str1):
                return lcp(str2, str1)
            
            pos = 0 

            while pos < len(str1):
                if str2[pos] == str1[pos]:
                    pos += 1
                else:
                    break
            
            return str1[:pos]

        LEN = len(strs)
        if LEN == 0: return ""

        result = strs[0]

        for i in range(1, LEN):
            result = lcp(result, strs[i])
        
        return result