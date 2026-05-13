class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0]]
        right = [height[-1]]

        for l in range(1, len(height)):
            app = max(left[l-1],height[l])
            left.append(app)
        i = 1

        for r in range(len(height)-2,-1,-1):
            app = max(right[i-1],height[r])
            i+=1
            right.append(app)
        res = 0;

        for i in range(1, len(height) - 1):
            
            res+= min(left[i], right[len(height) - 1 - i]) - height[i]
        return res    

   

