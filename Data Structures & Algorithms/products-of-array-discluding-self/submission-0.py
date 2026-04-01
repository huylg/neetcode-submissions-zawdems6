class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        numOfZero = 0

        for num in nums:
            if num != 0:
                product *= num
            else:
                numOfZero += 1

        if numOfZero > 1:
            return [0] * len(nums)

        result = []

        for num in nums:
            if num == 0 and numOfZero <= 1:
                result.append(product)
            elif numOfZero == 0:
                result.append(product // num)
            else:
                result.append(0)
        return result
