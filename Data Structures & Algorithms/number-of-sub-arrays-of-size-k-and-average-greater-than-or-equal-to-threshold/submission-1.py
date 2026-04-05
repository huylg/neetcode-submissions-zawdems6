class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        temp = 0

        for index, num in enumerate(arr):
            if index >= k:
                temp -= arr[index - k]

            temp += num
            if (temp / k) >= threshold and index >= k - 1:
                result += 1

        return result
