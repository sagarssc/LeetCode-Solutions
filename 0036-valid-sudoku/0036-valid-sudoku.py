class Solution:
    
    def check_grids(self,board):
        for i in range(3):
            for j in range(3):
                row = [board[x][y] for x in range(i*3,i*3+3) for y in range(j*3,j*3+3)]
                is_valid = self.is_valid(row)
                if not is_valid:
                    return False
        return True
    
    def check_columns(self, board):
        for row in zip(*board):
            is_valid = self.is_valid(row)
            if not is_valid:
                return False
        return True
    
    def check_rows(self,board):
        for row in board:
            is_valid = self.is_valid(row)
            if not is_valid:
                return False
        return True
    
    def is_valid(self, unit):
        unit = [i for i in unit if i!='.']
        return len(unit) ==len(set(unit))
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_rows(board) and self.check_columns(board) and self.check_grids(board)
        