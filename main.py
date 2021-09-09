from math import floor

class SudokuSolve(object):
    def solveSudoku(self, board):
        def is_valid(num, x, y):
            return valid_row(num, x) and valid_col(num, y) and valid_box(num, x, y)
            
        def valid_row(num, x):
            return num not in board[x]
        
        def valid_col(num, y):
            for x in range(9):
                if board[x][y] == num:
                    return False
            return True
        
        def valid_box(num, x, y):
            x = int(floor(x / 3.0) * 3)
            y = int(floor(y / 3.0) * 3)
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if board[i][j] == num:
                        return False
            return True
        
        nums = "123456789"
        
        def solve(x, y):
            if x == 9:
                return True
            cur = board[x][y]
            if cur == ".":
                for num in nums:
                    if is_valid(num, x, y):
                        board[x][y] = num
                        if y < 8:
                            if solve(x, y + 1):
                                return True
                        else:
                            if solve(x + 1, 0):
                                return True
                        board[x][y] = "."
            else:
                if y < 8:
                    if solve(x, y + 1):
                        return True
                else:
                    if solve(x + 1, 0):
                        return True
            return False
        
        solve(0, 0)
    
    def print_board(self, board):
        for i in range(9):
            if i == 3 or i == 6:
                print("---------------------")
            row = ""
            for j in range(9):
                if j == 3 or j == 6:
                    row += "| "
                row += board[i][j] + " " 
            print(row)