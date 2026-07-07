class Solution:
    def isDuplicated(self, nums: [str]) -> bool:
        s = set()

        for num in nums:
            if num != '.' and num in s:
                return True
            else:
                s.add(num)

        return False



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = 9
        
        for i in range(0,l):
            row = board[i]
            col = [ row[i] for row in board ]


            matrix = []

            for j in range(0,9):
                x = int(j / 3) + (i%3) *3
                y = (j % 3) + int(i/3) * 3
                print(x,y)
                value = board[x][y]
                matrix.append(value)


            if self.isDuplicated(row) or self.isDuplicated(col) or self.isDuplicated(matrix):
                return False
    

        return True

            





            

        return true

            