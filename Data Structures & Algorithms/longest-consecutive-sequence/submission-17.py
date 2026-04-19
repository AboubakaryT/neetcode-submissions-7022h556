class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        count = 0
        res = 0
        print(nums)
        
        if(len(nums) == 1 and nums[0] == 0):
            return 1
        elif (len(nums) == 1) or len(nums) == 0 :
            return 0    

        for i in range(len(nums) - 1):
            #How can I avoid index out of bounds?
            if nums[i+1] - nums[i] == 1:
                count+=1
            else:
                count = 0
            res = max(count, res)    
        return res + 1   