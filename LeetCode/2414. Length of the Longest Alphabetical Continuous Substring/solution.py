class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = start = 0
        for i in range(1, len(s)):
            if ord(s[i]) != ord(s[i - 1]) + 1:
                ans = max(ans, i - start)
                start = i  # 新起点
        return max(ans, len(s) - start)


作者：endlesscheng
链接：https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/solution/by-endlesscheng-rant/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        dp = [1]*n 
        ans = 1
        for i in range(1,n):
            if ord(s[i])-ord(s[i-1]) == 1:
                dp[i] += dp[i-1]
            ans = max(ans, dp[i])
        return ans