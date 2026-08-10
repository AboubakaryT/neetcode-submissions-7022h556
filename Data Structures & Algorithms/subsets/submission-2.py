class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []    
        #[1,2]
        #0, 1, 2
        def backtrack(i):
            if i == len(nums):
                res.append(sol[:])
                return
            
            backtrack(i+1)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res

            
