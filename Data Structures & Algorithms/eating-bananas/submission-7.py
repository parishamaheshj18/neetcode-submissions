import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles[i] - number of bananas in ith pile, len(piles) - how many piles
        # h - hours given to finish all the bananas
        # k - I have to decide bananas/hour - (sum(piles)/h)

        # [1] - 1
        # [4] - 2
        # [3] - 2
        # [2] - 1
        low = 1
        high = max(piles)
        res = high
        if h == len(piles):
            return high
        while low<=high:
            k_mid = (low+high)//2
            if self.is_k_ok(piles,k_mid,h) > 0:
                low = k_mid + 1
                
            elif self.is_k_ok(piles,k_mid,h) < 0:
                res = k_mid
                high = k_mid-1
            elif self.is_k_ok(piles,k_mid,h) == 0:
                res = k_mid
                high = k_mid -1
        return res
        

    def is_k_ok(self,piles,k,h):
        hours = 0
        for num in piles:
            hours += math.ceil(num / k)


        if hours > h:
            return 1
        elif hours < h:
            return -1
        elif hours==h:
            return 0

        
        
        

        

