class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        result = 0

        for num in s:
            if num - 1 not in s:
                next = num + 1
                while next in s:
                    next += 1 
                result = max(next - num, result)

        return result
