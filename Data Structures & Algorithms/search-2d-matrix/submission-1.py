class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        lo = 0
        hi = n * m - 1

        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            i = mid // m
            j = mid % m


            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return False
