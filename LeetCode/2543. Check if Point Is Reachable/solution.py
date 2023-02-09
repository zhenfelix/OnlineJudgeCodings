class Solution:
    def isReachable(self, x: int, y: int) -> bool:        
        while x%2 == 0:
            x //= 2
        while y%2 == 0:
            y //= 2
        if x == y:
            return x == 1
        if x > y:
            x, y = y, x 
        return self.isReachable(x,(x+y)//2)
