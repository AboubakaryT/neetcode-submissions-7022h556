class Solution:
    def findMin(self, nums: List[int]) -> int:
        l= 0
        r = len(nums)-1
        res = float('inf')
        #[3,0,5,6,1,2]
        #.      m
        while l <= r:
            m = (l + r )//2
            res = min(nums[m], res)
            if nums[m] < nums[r] :
                r = m 
            else:
                l = m+1
        return int(res)

