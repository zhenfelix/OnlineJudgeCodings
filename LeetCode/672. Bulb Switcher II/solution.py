class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if m == 0:
            return 1
        if m == 1:
            return min(4,n+1)
        else:
            mp = [1,2,4]
            if n < 3:
                return mp[n]
            return 7 if m == 2 else 8
            
        