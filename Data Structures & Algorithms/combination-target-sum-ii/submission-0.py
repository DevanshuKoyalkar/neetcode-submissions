class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # select or dont' select at each position

        candidates.sort()

        result = []
        LEN = len(candidates)

        def dfs(start, candidate_sum, candidate_list):
            if candidate_sum == target:
                result.append(candidate_list.copy())
                return

            if candidate_sum > target or start >= LEN:
                return
            
            

            cand = candidates[start]

            # select
            candidate_list.append(cand)
            dfs(start + 1, candidate_sum + cand, candidate_list)
            candidate_list.pop()

            # dont select
            next_idx = start + 1
            while next_idx < LEN and candidates[next_idx] == cand:
                next_idx += 1
            dfs(next_idx, candidate_sum, candidate_list)
        
        dfs(0, 0, [])

        return result
