class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        #rows
        for r in range(len(board)):
            row = []
            for c in range(len(board[r])):
                if board[r][c].isdigit():
                    if board[r][c] in row:
                        return False
                    row.append(board[r][c])

        #columns
        for r in range(len(board)):
            col = []
            for c in range(len(board)):
                if board[c][r].isdigit():
                    if board[c][r] in col:
                        return False
                    col.append(board[c][r])    

        #3x3
        for r in range(0,9,3):
            for c in range(0,9,3):
                #for box
                box = []
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if(board[j][i].isdigit()):
                            if board[j][i] in box:
                                return False
                            box.append(board[j][i])   
                        print(box) 


                    



        return True       