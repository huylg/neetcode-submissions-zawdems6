class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()

        for index, num in enumerate(nums):
            if index > k:
                s.remove(nums[index - k - 1])

            if num in s:
                return True

            s.add(num)

        return False
