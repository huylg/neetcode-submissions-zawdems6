class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [t[0] for t in  sorted(tuple(Counter(nums).items()),key=lambda x: x[1],reverse=True)[:k] ]
 