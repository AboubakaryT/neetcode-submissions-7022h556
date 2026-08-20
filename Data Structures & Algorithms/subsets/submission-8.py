class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(subset, i):
            if i == len(nums):
                res.append(subset[:])
                return
            dfs(subset, i+1)
            subset.append(nums[i])
            dfs(subset, i+1)
            subset.pop()

        dfs([], 0)
        return res