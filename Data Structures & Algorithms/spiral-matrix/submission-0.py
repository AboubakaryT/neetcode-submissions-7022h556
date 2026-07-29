class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        minCol, maxCol = 0, len(matrix[0])
        minRow, maxRow = 0, len(matrix)


        """
        minC,      maxC
        [1, 2, 3, 4]minR
        [5, 6, 7, 8]
        [9,10,11,12]maxR
        """
        row = 0
        res = []
        while minCol < maxCol and minRow < maxRow:
            #right
            for col in range(minCol, maxCol):
                res.append(matrix[row][col])
            minRow+=1
            #down
            for row in range(minRow, maxRow):
                res.append(matrix[row][col])
            maxCol-=1
            if minRow < maxRow and minCol < maxCol:
                #left
                for col in range(maxCol-1, minCol-1, -1):
                    res.append(matrix[row][col])
                maxRow-=1

                #up
                for row in range(maxRow-1, minRow-1, -1):
                    res.append(matrix[row][col])

                minCol+=1

        return res