class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        LEN = len(s)

        dp = [False] * (LEN + 1)
        dp[0] = True

        for i in range(1, LEN + 1):

            for j in range(i):
                dp[i] |= (s[j:i] in word_set and dp[j])

        # print(dp)
        return dp[LEN]
            