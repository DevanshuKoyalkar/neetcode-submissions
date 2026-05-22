class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if not len(stack):
                    return False
                
                if ch == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                
                if ch == ']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                
                if ch == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()



        return len(stack) == 0