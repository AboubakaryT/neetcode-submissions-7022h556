class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb = []
        res = []
        
        def dfs(i,total):
            if total > target:
                return

            elif total == target:
                res.append(comb[:])
                return
            if i == len(nums):
                return
            total+=nums[i]
            comb.append(nums[i])
            dfs(i,total)
            comb.pop()
            total-=nums[i]
            dfs(i+1,total)

        dfs(0,0)
        return res

            