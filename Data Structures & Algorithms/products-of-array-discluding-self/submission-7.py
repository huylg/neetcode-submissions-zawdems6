class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        number_of_zero = 0
        product = 1

        for num in nums:
            if num:
                product *= num
            else:
                number_of_zero += 1

        result = []

        for num in nums:

            if number_of_zero > 1 or (number_of_zero == 1 and num != 0 ):
                result.append(0)
            elif num == 0:
                result.append(product)
            else:
                result.append(int(product / num))
        return result

