class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for index, num in enumerate(nums):
            s[num] = index

        for i in range(len(nums) // 2 + 1):
            num = nums[i]
            looking = target - num
            if looking in s and s[looking] != i:
                return [i, s[looking]]
        return []

