class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = sys.maxsize
        lo = 0
        temp = 0

        for hi, num in enumerate(nums):
            temp += num

            while temp >= target and lo <= hi:
                result = min(result, hi - lo + 1)
                temp -= nums[lo]
                lo += 1

        return 0 if result == sys.maxsize else result
