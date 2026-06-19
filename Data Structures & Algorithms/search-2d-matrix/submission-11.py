class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0

        while l <= len(matrix) - 1:
            x = 0
            y = len(matrix[l])-1
            
            if matrix[l][x] < target and matrix[l][y] < target:
                l+=1
            elif matrix[l][x] <= target and target <= matrix[l][y]:
                while x <= y or x == y:
                    m = (x + y)//2
                    if matrix[l][m] == target:
                        return True
                    elif matrix[l][m] < target:
                        x = m+1
                    elif matrix[l][m] > target:
                        y = m-1
                return False
            elif matrix[l][x] >= target :
                return False
        
        return False
        
        #matrix = [[1,3,5,7],[10,11,16,20]], target = 99