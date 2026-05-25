class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OPERATORS = "+-*/"

        stack = []
        for token in tokens:
            if token in OPERATORS:
                second = int(stack.pop())
                first = int(stack.pop())

                # print(first, second, token)

                if token == '+':
                    stack.append(first + second)
                elif token == '-':
                    stack.append(first - second)
                elif token == '*':
                    stack.append(first * second)
                else:
                    stack.append(int(first/second))
            else:
                stack.append(int(token))
        
        return stack[-1]