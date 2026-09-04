class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = 0 # most repeat character
        d = {}
        l = 0

        result = 0

        for r, v in enumerate(s):

            d[v] = d.get(v, 0) + 1
            c = max(c, d[v])

            while (r - l + 1) - c > k:
                d[s[l]] -= 1
                l+=1
                c = max(c, d[s[l]])


            result =  max(r - l + 1, result)

        return result
