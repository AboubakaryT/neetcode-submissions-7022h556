class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        each bar width = 1
        use the smallest bar as the max height of the rectangle.
        Rectangle can either be vertical or horizontal.(Tricky!)
        Formula = height(lowest) * amount of indices involved.
        """
        n = len(heights)
        res = 0
        for i in range(n):
            height = heights[i]
            rightMost = i + 1
            leftMost = i
            while rightMost < n and heights[rightMost] >= height:
                rightMost+=1
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost-=1
            
            rightMost -= 1
            leftMost += 1
            res = max(res, height * (rightMost - leftMost + 1))
        return res  
        


          #  
          #  
          #  
          #   
         ##
         ##       
        ###      