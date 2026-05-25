class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def dfs(open_left, close_left, cand):
            if open_left > close_left:
                return

            if open_left == 0 and close_left == 0:
                result.append("".join(cand.copy()))
                return
            
            # put an open
            if open_left > 0:
                cand.append('(')
                dfs(open_left - 1, close_left, cand)
                cand.pop()

            # put a close
            if close_left > 0:
                cand.append(')')
                dfs(open_left, close_left - 1, cand)
                cand.pop()
        
        dfs(n, n, [])

        return result