class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visit = [-1] * len(nums)

        for num in nums:
            if visit[num] == -1:
                visit[num] = 1
            else:
                return num

           
        
