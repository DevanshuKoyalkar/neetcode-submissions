class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     word_set = set(wordDict)

    #     LEN = len(s)

    #     dp = [False] * (LEN + 1)
    #     dp[0] = True

    #     for i in range(1, LEN + 1):

    #         for j in range(i):
    #             dp[i] |= (s[j:i] in word_set and dp[j])

    #     # print(dp)
    #     return dp[LEN]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string can always be segmented
        
        for i in range(n):
            if not dp[i]:
                continue  # Skip if the prefix s[:i] cannot be formed
                
            # Only check the actual words instead of slicing every index
            for word in wordDict:
                word_len = len(word)
                # If the word fits and matches the substring ahead, mark it valid
                if i + word_len <= n and s[i:i + word_len] == word:
                    dp[i + word_len] = True
                    
        return dp[n]
            