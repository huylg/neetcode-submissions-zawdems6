class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lo = 0
        c2 = {}
        c1 = Counter(s1)

        for hi, c in enumerate(s2):
            c2[c] = c2.get(c, 0) + 1

            if hi - lo + 1 == len(s1) and c1[c] == c2[c]:
                return True

            while c2[c] > c1[c]:
                c2[s2[lo]] -= 1
                lo += 1

        return False

