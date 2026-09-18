class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newNums = [0] * (len(nums) * 2)
        i = 0
        while i < len(newNums):
            for j in range(len(nums)):
                newNums[i] = nums[j]
                i+=1
            
        return newNums