class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9+7
        n = len(num2)
        if len(num1) < n:
            num1 = '0'*(n-len(num1))+num1

        @lru_cache(None)
        def dfs(i,lo,hi,s):
            if s > max_sum:
                return 0 
            if i == n:
                return min_sum <= s
            mi = int(num1[i]) if lo else 0 
            mx = int(num2[i]) if hi else 9
            ans = 0 
            for ch in range(mi,mx+1):
                ans += dfs(i+1,lo and ch == mi, hi and ch == mx, s+ch)
            return ans%MOD 
        return dfs(0,True,True,0)

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9+7
        n = max(len(num1),len(num2))
        if len(num1) < n:
            num1 = '0'*(n-len(num1))+num1
        if len(num2) < n:
            num2 = '0'*(n-len(num2))+num2
        @lru_cache(None)
        def dfs(i,lo,hi,s):
            if i == n:
                return min_sum <= s <= max_sum
            if s > max_sum:
                return 0 
            mi = int(num1[i]) if lo else 0 
            mx = int(num2[i]) if hi else 9
            ans = 0 
            for ch in range(mi,mx+1):
                ans += dfs(i+1,lo and ch == mi, hi and ch == mx, s+ch)
            return ans%MOD 
        return dfs(0,True,True,0)