class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        l = 1
        r = len(nums) - 1
        nums = sorted(nums)

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if (nums[l] + nums[i] + nums[r]) == 0:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l+=1
                    r-=1
                elif l<r and  (nums[l] + nums[i] + nums[r]) > 0:
                    r-=1
                elif l<r and (nums[l] + nums[i] + nums[r]) < 0:
                    l+=1  

        return list(res)           
            

