class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position, speed)]

        pairs.sort()

        stack = []
        for p,s in pairs[::-1]:
            dest_time = (target - p) / s

            if stack:
                prev_pos, prev_speed = stack[-1]
                prev_dest_time = (target - prev_pos) / prev_speed

                if dest_time > prev_dest_time:
                    stack.append((p,s))
            
            else:
                stack.append((p,s))
        
        return len(stack)


