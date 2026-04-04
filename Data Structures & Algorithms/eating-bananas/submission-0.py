class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        result = hi = max(piles)

        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                result = min(mid, result)
                hi = mid - 1
            else:
                lo = mid + 1

        return result
   