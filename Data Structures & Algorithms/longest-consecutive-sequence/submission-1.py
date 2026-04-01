class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        result = 0
        for num in s:
            if num - 1 in s:
                continue
            temp = 0
            while num + temp in s:
                temp += 1
            result = max(temp, result)
                
        return result


        