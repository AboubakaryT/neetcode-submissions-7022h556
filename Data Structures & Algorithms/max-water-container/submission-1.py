class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #[1,7,2,5,4,7,3,6]
        #We are essentially returning the windowsize * (The smallest of the two heights)
        res = 0 
        l = 0
        r= len(heights) - 1
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res,area)
            if(l<r and heights[l] < heights[r]):
                l+=1
            else:
                r-=1    

        return res