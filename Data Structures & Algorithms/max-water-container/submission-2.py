class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0

        while l < r:
            res = max((r - l) * min(heights[l], heights[r]), res)
            if heights[l] >= heights[r]:
                r-=1
            elif heights[r] >= heights[l]:
                l+=1
        return res 

        
            