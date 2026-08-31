class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        numberOfZeros = 0
        prod = 1

        for num in nums:
            if num:
                prod *= num
            else:
                numberOfZeros += 1

        for num in nums:
            if numberOfZeros > 1 or (numberOfZeros == 1 and num != 0):
                result.append(0)
            elif num == 0:
                result.append(prod)
            else:
                result.append(prod//num)

        return result
