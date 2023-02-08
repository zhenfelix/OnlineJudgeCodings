# class Solution:

#     def maxPalindromes(self, s: str, k: int) -> int:

#         L = manacher('#' + ''.join(ch + '#' for ch in s))

#         dp = [0] * (len(s) * 2 + 1)

#         for i, ln in enumerate(L):

#             if dp[i] < dp[i - 1]: dp[i] = dp[i - 1]

#             if ln < k: continue

#             l, r = i - k - ((i - k) & 1), i + k

#             if dp[r] < dp[l] + 1: dp[r] = dp[l] + 1

#         return dp[-1]

# 作者：不造轮子
# 链接：https://leetcode.cn/problems/maximum-number-of-non-overlapping-palindrome-substrings/solutions/1965439/by-freeyourmind-g85h/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ss = '*'.join(list(s))
        m = len(ss)
        dp = [0]*(n+1)
        sz = [1]*m 
        l = r = 0
        for i in range(m):
            if i <= r:
                sz[i] = min(sz[l+r-i],r-i+1)
            if i+sz[i]-1 >= r: 
                while i+sz[i] < m and i-sz[i] >= 0 and ss[i+sz[i]] == ss[i-sz[i]]:
                    sz[i] += 1
            if i+sz[i]-1 > r:
                l, r = i-sz[i]+1, i+sz[i]-1
            lo, hi = i-sz[i]+1, i+sz[i]-1
            lo = (lo+1)//2
            hi = hi//2
            # print(i,lo,hi)
            if hi-lo+1 >= k:
                delta = (hi-lo+1-k)//2
                hi -= delta
                lo += delta
                dp[hi+1] = max(dp[hi+1],dp[lo]+1)
            if i%2:
                j = i//2
                if j+2 <= n:
                    dp[j+2] = max(dp[j+2],dp[j+1])
        # print(dp)
        return dp[-1]


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0]*(n+1) 
        for i in range(k,n+1):
            dp[i] = dp[i-1]
            for j in range(max(i-k-1,0),i-k+1)[::-1]:
                if s[j:i] == s[j:i][::-1]:
                    dp[i] = max(dp[i], dp[j]+1)
                    break
        return dp[-1]



class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dfs(i,j):
            if i >= j:
                return True
            if s[i] == s[j] and dfs(i+1,j-1):
                return True
            return False


        dp = [0]*(n+1) 
        for i in range(k,n+1):
            dp[i] = dp[i-1]
            for j in range(i-k+1)[::-1]:
                if dfs(j,i-1):
                    dp[i] = max(dp[i], dp[j]+1)
                    break
        dfs.cache_clear()
        return dp[-1]


def memo(f):
    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)
        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret 
    return memodict().__getitem__

#DIY cache decorator without cache_clear will be TLE
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        n = len(s)
        @memo
        def dfs(i,j):
            if i >= j:
                return True
            if s[i] == s[j] and dfs(i+1,j-1):
                return True
            return False


        dp = [0]*(n+1) 
        for i in range(k,n+1):
            dp[i] = dp[i-1]
            for j in range(i-k+1)[::-1]:
                if dfs(j,i-1):
                    dp[i] = max(dp[i], dp[j]+1)
                    break
        # dfs.cache_clear()
        return dp[-1]




class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        p = [[False]*n for _ in range(n)]
        for i in range(n):
            p[i][i] = True
            if i:
                p[i][i-1] = True
        for i in range(n)[::-1]:
            for j in range(i+1,n):
                if s[i] == s[j] and p[i+1][j-1]:
                    p[i][j] = True 

        dp = [0]*(n+1) 
        for i in range(1,n+1):
            dp[i] = dp[i-1]
            for j in range(i):
                if p[j][i-1] and i-j >= k:
                    dp[i] = max(dp[i], dp[j]+1)
        return dp[-1]
