class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #nums = [2,-3,4,-2,2,1,-1,4]
        currSum = 0
        res = float("-inf")
           
        for n in nums:
            currSum+=n
            res = max(currSum, res)
            if currSum < 0:
                currSum = 0
                
        return res
