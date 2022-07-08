from functools import lru_cache
class Solution:
    def sellingWood(self, h: int, w: int, prices: List[List[int]]) -> int:
        mp = defaultdict(int)
        for hh, ww, p in prices:
            mp[hh,ww] = p 

        @lru_cache(None)
        def dfs(i,j):
            if i == 1 and j == 1:
                return mp[i,j]
            ans = mp[i,j]
            for ii in range(1,i):
                ans = max(ans, dfs(ii,j)+dfs(i-ii,j))
            for jj in range(1,j):
                ans = max(ans, dfs(i,jj)+dfs(i,j-jj))
            return ans 
        return dfs(h,w)



class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n, m = len(s), k.bit_length()
        if n < m: return n
        ans = m if int(s[n - m:], 2) <= k else m - 1
        return ans + s.count('0', 0, n - m)


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/longest-binary-subsequence-less-than-or-equal-to-k/solution/fen-lei-tao-lun-tan-xin-by-endlesscheng-vnlx/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。