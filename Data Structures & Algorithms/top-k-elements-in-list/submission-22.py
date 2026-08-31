class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in heapq.nlargest(k, Counter(nums).items(), lambda x: x[1])]

