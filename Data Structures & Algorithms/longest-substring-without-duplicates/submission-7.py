class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        d = {}

        result = 0

        for r in range(len(s)):

            if s[r] in d and l <= d[s[r]]:
                l = d[s[r]] + 1


            result=max(result, r - l + 1)
            d[s[r]] = r

        return result



