import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high

        while low <= high:
            k = (low + high) // 2
            status = self.is_k_ok(piles, k, h)
            if status > 0:          # too slow → need bigger k
                low = k + 1
            else:                   # k works (≤ h) → try smaller k
                res = k
                high = k - 1
        return res

    def is_k_ok(self, piles, k, h):
        hours = 0
        for num in piles:
            hours += math.ceil(num / k)
        if hours > h:
            return 1
        else:
            return -1   # we don't need separate 0; just re