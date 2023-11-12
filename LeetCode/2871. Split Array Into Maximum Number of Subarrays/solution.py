class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        m = 25
        idx = [-1]*m 
        dp = [0]*(n+1)
        for i, v in enumerate(nums):
            for j in range(m):
                if (v>>j)&1: continue
                idx[j] = max(idx[j],i)
            k = min(idx)
            if k >= 0:
                dp[i] = max(dp[i],dp[k-1]+1)
            dp[i] = max(dp[i],dp[i-1])
        return 1 if dp[n-1] == 0 else dp[n-1]

# 另一种写法：
class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        cnt = 0
        curr = (1 << 20) - 1
        for num in nums:
            curr &= num
            if curr == 0: cnt += 1; curr = (1 << 20) - 1
        return max(cnt, 1)

作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/slLdgm/view/ytByYQ/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。