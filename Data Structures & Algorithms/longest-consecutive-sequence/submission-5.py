class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        lows = []
        s = set(nums)

        for num in s:
            if num - 1 not in s:
                lows.append(num)

        result = 0

        for low in lows:
            hi = low
            while hi + 1 in s:
                hi+=1
            result = max(result,hi-low+1)

        return result
