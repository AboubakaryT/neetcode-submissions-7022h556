class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        pac,atl = set(), set()

        def dfs(r,c,visit,prevHeight):
            if r == ROW or r < 0 or c == COL or c < 0 or (r,c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            prevHeight = heights[r][c]

            dfs(r+1,c, visit, prevHeight)
            dfs(r,c+1, visit, prevHeight)
            dfs(r-1,c, visit, prevHeight)
            dfs(r,c-1, visit, prevHeight)
            return visit

        for c in range(COL):
            #CALL DFS ON FIRST ROW
            dfs(0, c, pac, heights[0][c])
            #CALL DFS ON LAST ROW
            dfs(ROW-1, c, atl, heights[ROW-1][c])

        for r in range(ROW):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COL-1,atl,heights[r][COL-1])

        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res