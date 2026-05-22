class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in lookup:
                if not stack or stack[-1] != lookup[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)



        return len(stack) == 0