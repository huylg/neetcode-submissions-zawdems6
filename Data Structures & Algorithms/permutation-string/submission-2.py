class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0

        d = defaultdict(int)

        for c in s1:
            d[c] += 1


        for r, v in enumerate(s2):

            d[v] -= 1

            while d[v] < 0:
                d[s2[l]] += 1
                l += 1

            if (r - l + 1 == len(s1)):
                return True


        return False
