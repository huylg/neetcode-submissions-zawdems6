class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        l= len(nums)

        result = []

        for i in range(l):
            left, right = i+1, l - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                value =  nums[i] + nums[left] + nums[right]

                if value == 0:
                    result.append([nums[i], nums[left] , nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1


                elif value < 0:
                    left += 1
                else:
                    right -= 1

        return result

