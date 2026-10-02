class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = [0]
        ROW = len(grid)
        COL = len(grid[0])

        def dfs(r,c):
            #[1,1]
            if COL == c or c < 0 or ROW == r or r < 0 or grid[r][c] == 0:
                return 0
                
            grid[r][c] = 0
            count = 1 + dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)
            res[0] = max(count,res[0])
            return count
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i,j)
        return res[0]