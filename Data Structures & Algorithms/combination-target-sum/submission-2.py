class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, comb, count):
            if count == target:
                res.append(comb[:])
                return
            elif i >= len(nums) or count > target:
                return
                
            comb.append(nums[i])
            dfs(i, comb, count+nums[i])
            comb.pop()
            count-=nums[i]
            dfs(i+1, comb, count+nums[i])

        dfs(0, [], 0)
        return res
