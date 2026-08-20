class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        At every single cell we must check if at the letters match up. If they do we return true. else we return false.
        """
        visited = set()
        row = len(board)
        col = len(board[0])
        def backtrack(r,c,i):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= row or c >= col or (r,c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r,c))
            res = backtrack(r+1, c, i+1) or backtrack(r-1, c, i+1) or backtrack(r, c+1, i+1) or backtrack(r, c-1, i+1)
            visited.remove((r,c))
            return res

        for r in range(row):
            for c in range(col):
                if backtrack(r,c,0):
                    return True

        return False