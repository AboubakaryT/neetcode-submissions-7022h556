class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        1  2  3  4
        5  6  7  8
        9 10 11 12

        left = 1
        right = 2

        top = 2
        bottom = 1
        """
        res = []
        top = 0
        right = len(matrix[0]) - 1
        left = 0
        bottom = len(matrix) - 1
        
        while left <= right and top <= bottom:
            #left
            for c in range(left, right+1):
                res.append(matrix[top][c])
            #close the top off
            top+=1
            
            #down
            for r in range(top, bottom+1):
                print(right)
                res.append(matrix[r][right])
            #close the right side
            right-=1

            #left
            if left <= right and top <= bottom:
                for c in range(right, left-1, -1):
                    res.append(matrix[bottom][c])
                #close the bottom
                bottom-=1

                #up
                for r in range(bottom, top-1, -1):
                    res.append(matrix[r][left])
                #close the left 
                left+=1
            
        return res
        """
        #Was stuck on the last if, we want to protect the invariant. After we traverse left again there may not be a rectangle to traverse anymore, hence the if statement.
        """



