class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        low = 0

        result = 0

        for hi, num in enumerate(arr):

            if (
                (hi == low)
                or (hi == low + 1 and arr[hi] != arr[low])
                or (arr[hi - 1] < num and arr[hi - 1] < arr[hi - 2])
                or (arr[hi - 1] > num and arr[hi - 1] > arr[hi - 2])
            ):
                continue
            else:
                result = max(result, hi - low)
                low = hi - 1 if arr[hi] != arr[low] else hi

        return max(result, len(arr) - low)

             
