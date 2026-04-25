class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #[1,7,2,5,4,7,3,6]
        #We are essentially returning the windowsize * (The smallest of the two heights)
        res = 0 
        for l in range(len(heights)):
            for r in range(l+1, len(heights)):
                area = (r-l) * min(heights[l], heights[r])
                res = max(res,area)

        return res