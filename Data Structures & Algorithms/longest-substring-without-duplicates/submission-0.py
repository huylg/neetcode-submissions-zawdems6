class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        se = set()
        lo = 0

        for hi, c in enumerate(s):
            while c in se:
                se.remove(s[lo])
                lo += 1

            se.add(c)

            result = max(result, hi - lo + 1)

        return result
   