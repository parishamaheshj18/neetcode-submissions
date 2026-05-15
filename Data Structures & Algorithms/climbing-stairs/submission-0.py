class Solution:
    def __init__(self):
        self.map = {}
    def climbStairs(self, n: int) -> int:
        if n<=2:
            self.map[n] = n
            return n
        if n in self.map:
            return self.map[n]
        
        self.map[n] = self.climbStairs(n-1) + self.climbStairs(n-2) 
        return self.map[n]