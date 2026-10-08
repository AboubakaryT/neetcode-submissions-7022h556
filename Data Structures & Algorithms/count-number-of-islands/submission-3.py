class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROW = len(grid)
        COL = len(grid[0])

        def dfs(r,c):
            if r < 0 or r == ROW or c < 0 or c == COL or grid[r][c] == "0":
                return 

            if grid[r][c] == "1":
                grid[r][c] = "0"

            dfs(r+1, c) 
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r,c-1)
            

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res+=1
        return res

        """
        [['0', '0', '0', '0', '1']
         ['0', '0', '0', '0', '1'],
         ['0', '0', '0', '0', '0'], 
         ['0', '0', '0', '0', '1']]
        """
