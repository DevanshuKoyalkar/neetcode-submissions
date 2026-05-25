class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        LEN = len(temperatures)
        stack = []
        result = [0] * LEN

        for curr_idx, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = curr_idx - prev_idx
            
            stack.append(curr_idx)
        
        return result
                

