class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9

        for i in range(size):
            counters = [
                Counter(board[i]),
                Counter([board[j][i] for j in range(size)]),
                Counter(
                    [board[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3] for j in range(size)]
                ),
            ]

            for counter in counters:
                for num, count in counter.items():
                    if num != "." and count > 1:
                        return False
        return True
   


