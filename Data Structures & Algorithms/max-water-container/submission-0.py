class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low, high = 0, len(heights) - 1
        result = 0

        while low < high:
            area = min(heights[low], heights[high]) * (high - low)
            result = max(result, area)

            if heights[low] < heights[high]:
                low += 1
            elif heights[low] > heights[high]:
                high -= 1
            else:
                low += 1
                high -= 1

        return result