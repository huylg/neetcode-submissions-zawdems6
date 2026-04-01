class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        le = len(nums)
        arr = [0] * le * 2
        for i in range(le * 2):
            arr[i] = nums[i % le]
        return arr
    