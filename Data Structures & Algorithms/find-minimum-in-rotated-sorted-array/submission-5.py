class Solution:
    def findMin(self, nums: List[int]) -> int:
        l= 0
        r = len(nums)-1
        res = float('inf')
        #[3,0,5,6,1,2]
        #l     m    r
        
        while l <= r:
            m = (l + r)//2
           
            res = min(nums[m], res)
            if nums[r] > nums[m]:
                r = m-1
            else:
                l = m+1
        return int(res)

        
