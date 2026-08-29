class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()
        ROW, COL = len(board), len(board[0])


        def dfs(r,c,visit):
            if r == ROW or c == COL or r < 0 or c < 0 or (r,c) in visit or board[r][c] == "X":
                return

            if board[r][c] == "O":
                visit.add((r,c))
                dfs(r+1,c,safe)
                dfs(r,c+1,safe)
                dfs(r-1,c,safe)
                dfs(r,c-1,safe)
                
            return visit

        for c in range(COL):
                dfs(0,c,safe)
                dfs(ROW-1,c,safe)

        for r in range(ROW):
                dfs(r,0,safe)
                dfs(r, COL-1, safe)
        
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in safe and board[r][c] != "X":
                    board[r][c] = "X"
            