class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [ x for x in board[i] if x != '.' ]
            col = [row[i] for row in board if row[i] != '.'] 
            matrix = []
            for j in range(9):
                x = (i//3)*3 + (j // 3)
                y = (i%3)*3 + (j % 3)
                value = board[x][y]
                if value != '.':
                    matrix.append(board[x][y])

            for x in [row, col, matrix]:
                l = len(x)
                l_s = len(set(x))

                if(l != l_s):
                    return False


        return True
