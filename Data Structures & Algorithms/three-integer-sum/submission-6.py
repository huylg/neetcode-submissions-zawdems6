class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        s = { value: index for index, value in enumerate(nums) }

        l = len(nums)
        triplets= []

        for i in range(l):
            a = nums[i]
            
            for j in range (i+1, l):
                b = nums[j]

                target = s.get(-a-b,-1)
                if target > i and target > j:
                    triplets.append([a,b,-a-b])


        unique = set([tuple(sorted(arr)) for arr in triplets])
        return [list(s) for s in unique]
