from collections import deque as dq
class Solution:
        
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        visit = set()
        queue = dq()
        def addRooms(r,c):
            if r == ROW or c == COL or r < 0 or c < 0 or (r,c) in visit or grid[r][c] == -1: 
                return
            else:
                visit.add((r,c))
                queue.append([r,c])
                
        #Append the gates so we can simulatneous do BFS for each gate.
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visit.add((r,c))
        dist = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = dist
                addRooms(r+1,c)
                addRooms(r,c+1)
                addRooms(r-1,c)
                addRooms(r,c-1)
      
            dist+=1

        