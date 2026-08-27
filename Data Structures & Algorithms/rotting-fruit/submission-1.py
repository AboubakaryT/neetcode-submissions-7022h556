from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        visit = set()
        def addToQueue(r,c):
            if r == ROW or c == COL or r < 0 or c < 0 or (r,c) in visit:
                return
            elif grid[r][c] == 1:
                grid[r][c] = -1
                visit.add((r,c))
                queue.append([r,c])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append([r,c])
                    visit.add((r,c))
        res = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                addToQueue(r+1,c)
                addToQueue(r,c+1)
                addToQueue(r-1,c)
                addToQueue(r,c-1)
            if queue:
                res+=1
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return -1
        return res 


        """
        [2,1,1]
        [0,1,1]
        [1,0,1]
        """