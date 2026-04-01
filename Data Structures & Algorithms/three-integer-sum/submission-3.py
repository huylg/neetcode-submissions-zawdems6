class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        nums = sorted(numbers)

        l = len(nums)

        result = []

        for i in range(l - 2):
            num = nums[i]

            if i > 0 and num == nums[i - 1]:
                continue

            low, high = i + 1, l - 1

            while low < high:
                if num + nums[low] + nums[high] == 0:
                    result.append((num, nums[low], nums[high]))
                    low += 1
                    high -= 1
                elif num + nums[low] + nums[high] < 0:
                    low += 1
                else:
                    high -= 1

        return list(set(result))