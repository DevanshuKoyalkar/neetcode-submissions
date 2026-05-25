class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        LEN = len(temperatures)
        result = [0] * LEN

        for pos, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                result[stack[-1][1]] = pos
                stack.pop()
            
            stack.append((temp, pos))
        
        for i in range(LEN):
            if result[i]: 
                result[i] -= i
        
        return result
                

