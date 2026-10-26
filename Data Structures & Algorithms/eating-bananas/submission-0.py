class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def hours(k):
            total = 0
            for pile in piles:

                total += (pile + k - 1) // k
            return total
            
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if hours(mid) <= h: hi = mid
            else: lo = mid + 1
        return lo