class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        ans = 0
        for i, ch in enumerate(s):
            val = int(ch)
            for j in range(i+1)[::-1]:
                if dp[j]*2+val < min(dp[j+1], k+1):
                    dp[j+1] = dp[j]*2+val
                if dp[j+1] <= k:
                    ans = max(ans, j+1)
        return ans 



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