class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lo = max_req = 0

        dict = {}

        for hi, c in enumerate(s):
            dict[c] = dict.get(c, 0) + 1
            max_req = max(max_req, dict[c])

            if hi - lo + 1 - max_req > k:
                dict[s[lo]] -= 1
                lo += 1

        return min(max_req + k, len(s))
