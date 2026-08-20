class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #O(n log n for sorting)
        candidates = sorted(candidates)
        res = []
        comb = []
        count = [0]
        #[1,2,2,4,5,6,9]
        def dfs(i):
            if count[0] == target:
                res.append(comb[:])
            elif count[0] > target or i >= len(candidates):
                return
            

            #loop so that we don't reuse values.
            for j in range(i, len(candidates)):
                if i != j and j < len(candidates) and candidates[j] == candidates[j-1]:
                    continue
                 
                comb.append(candidates[j])
                count[0]+= candidates[j]
                dfs(j+1)
                comb.pop()
                count[0]-=candidates[j]
               




        dfs(0)
        return res