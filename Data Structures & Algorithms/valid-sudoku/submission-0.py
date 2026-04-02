from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Columns, and Rows, as
        well as boxes  must not 
        contain any duplicates
        """
        col = defaultdict(set)
        row = defaultdict(set)
        box = defaultdict(set)  #Row / 3, Column / 3

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in box[(r // 3, c // 3)]):
                    return False 
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                box[r//3, c//3].add(board[r][c])   
        return True                   