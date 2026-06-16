class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            hm = {}
            #[3,2,4]
            #hm = {3:0, 2:1, 4:2}
            
            for i, n in enumerate(nums):
                complement = target - n
                if complement in hm:
                    return [hm[complement], i]
                hm[n] = i 
            
        