class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROW = len(grid)
        COL = len(grid[0])
        def dfs(r,c):
            nonlocal res
            if ROW == r or COL == c or r < 0 or c < 0 or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            maxArea = 1 + dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)
            return maxArea


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    res = max(res,dfs(r,c))
        return res