class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        i = 2
        while i < len(costs):
            costs[i] += min(costs[i - 1] , costs[i - 2])
            i += 1

        return min(costs[-1], costs[-2])
