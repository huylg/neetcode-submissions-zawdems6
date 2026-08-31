class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        s = {}

        for i,num in enumerate(nums):
            s[num] = i

        for i,num in enumerate(nums):
            j = s.get(target - num, i)

            if i != j:
                return [i, j]
        


