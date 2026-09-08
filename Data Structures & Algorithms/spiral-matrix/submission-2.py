class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        [1, 2, 3, 4]
        [5, 6, 7, 8]
        [9,10,11,12]
        [13,14,15,16]
        """
        top, bottom = 0, len(matrix)-1
        left,right = 0, len(matrix[0])-1
        res = []
        #left
        #1, 2
        while left <= right and top <= bottom:
            for r in range(left, right+1):
                res.append(matrix[top][r])
            top+=1

            for d in range(top, bottom+1):
                res.append(matrix[d][right])
            right-=1

            if left <= right and top <= bottom:
                for l in range(right, left-1, -1):
                    res.append(matrix[bottom][l])
                    print(matrix[bottom][l])
                    print(f"bottom:{bottom}")
                bottom-=1

                for t in range(bottom, top-1, -1):
                    res.append(matrix[t][left])
                left+=1

        return res