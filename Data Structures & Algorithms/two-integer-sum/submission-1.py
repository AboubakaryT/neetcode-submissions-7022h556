class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We want to take two numbers and return both of them if their sum = target
        #We want to return the first result of this.
        #Using a hashmap provides O(1) lookup.

        hm = {}
        #complement = 4 -> 3 ->2 -> 1
        #hm = 3:0, 4:1, 5:2, 6:3
        for i, v in enumerate(nums):
            complement = target - v
            if complement in hm:
                return[hm[complement], i]
            hm[v] = i    