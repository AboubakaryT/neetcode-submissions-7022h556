class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        maxArea = 0
        def dfs(r,c,area):
            if r < 0 or c < 0 or r == ROW or c == COL or grid[r][c] == 0:
                return 0
            area+=1
            grid[r][c] = 0
            area = 1 + dfs(r+1,c,area) + dfs(r,c+1,area) + dfs(r-1,c,area) + dfs(r,c-1,area)
            return area
            



        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    maxArea = max(dfs(r,c,0), maxArea)

                    
        return maxArea
        

        """
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
        """
            
