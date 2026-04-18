class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
    
        temp = [1,2]
        for i in range(2,n):
            temp.append (temp[i-1]+temp[i-2])
        return temp[-1]

