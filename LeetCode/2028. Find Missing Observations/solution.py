class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        tot = mean*(n+len(rolls))-sum(rolls)
        if tot > 6*n or tot < n:
            return []
        res = []
        while n:
            for i in range(1,7):
                if (n-1) <= tot-i <= 6*(n-1):
                    res.append(i)
                    tot -= i 
                    n -= 1
                    break
        return res


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        tot = mean*(n+len(rolls))-sum(rolls)
        if tot > 6*n or tot < n:
            return []
        res = []
        cur = 1
        while n:
            while not ((n-1) <= tot-cur <= 6*(n-1)):
                cur += 1
            res.append(i)
            tot -= i 
            n -= 1
        return res


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        tot = mean*(n+len(rolls))-sum(rolls)
        if tot > 6*n or tot < n:
            return []
        res = [tot//n]*n
        tot %= n
        i = 0
        while tot:
            res[i] += 1
            i += 1
            tot -= 1
        return res