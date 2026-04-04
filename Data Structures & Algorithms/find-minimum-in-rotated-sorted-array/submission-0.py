class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            print(nums[lo], nums[mid], nums[hi])
            if nums[lo] <= nums[mid] and nums[mid] <= nums[hi]:
                return nums[lo]
            elif nums[lo] > nums[mid]:
                hi = mid
            else:
                lo = mid + 1

        return -1
