class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (hi - lo) // 2 + lo

            if nums[mid] == target:
                return mid
            elif nums[lo] < nums[mid] and target < nums[mid] and target >= nums[lo]:
                hi = mid - 1
            elif nums[lo] > nums[mid] and (target >= nums[lo] or target < nums[mid]):
                hi = mid - 1
            else:
                lo = mid + 1

        return -1
   