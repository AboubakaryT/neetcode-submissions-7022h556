class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        count = [0]
        def dfs(i):
            #base cases
            if len(nums) == i or count[0] > target:
                return
            elif count[0] == target:
                res.append(comb[:])
                return
           
            comb.append(nums[i])
            count[0]+=nums[i]
            dfs(i)
            comb.pop()
            count[0]-=nums[i]

            dfs(i+1)

        dfs(0)
        return res