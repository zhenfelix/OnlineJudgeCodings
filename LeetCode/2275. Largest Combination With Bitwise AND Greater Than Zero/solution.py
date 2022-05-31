class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        dp = [0]*30
        ans = 0
        for x in candidates:
            for i in range(30):
                if (x>>i)&1:
                    dp[i] += 1
                    ans = max(ans, dp[i])
        return ans


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max(sum((num >> i) & 1 for num in candidates) for i in range(24))


作者：endlesscheng
链接：https://leetcode.cn/problems/largest-combination-with-bitwise-and-greater-than-zero/solution/by-endlesscheng-dwja/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。