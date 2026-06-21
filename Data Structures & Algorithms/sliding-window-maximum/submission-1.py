class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        res= []
        while r < len(nums):
            maxK = float("-inf")
            for j in range(l, r+1):
                maxK = max(maxK, nums[j])
            res.append(maxK)
            l +=1
            r+=1
        return res
        
    