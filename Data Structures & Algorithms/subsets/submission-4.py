class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []    
        #[1,2]
        #1, 2
        def dfs(i):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

            
        dfs(0)
        return res

            
