class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        """
        []
         |
         V
        [1]
         |
         V
       [1,2]
         |
         V                     
      [1,1]
        
        """
        nums = sorted(nums)
        def dfs(i, subset):
            if i == len(nums):
                return
            subset.append(nums[i])
            res.append(subset[:])
            dfs(i+1, subset)
            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1,subset)
                
            
           
        dfs(0, [])
            
        return res
            
