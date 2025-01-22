class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        mx = max(nums)
        max_d = mx - min(nums)
        f = [[0] * (max_d + 2) for _ in range(len(nums))]
        last = [-1] * (mx + 1)
        for i, x in enumerate(nums):
            for j in range(max_d, -1, -1):
                f[i][j] = max(f[i][j + 1], 1)
                if x - j >= 0 and last[x - j] >= 0:
                    f[i][j] = max(f[i][j], f[last[x - j]][j] + 1)
                if x + j <= mx and last[x + j] >= 0:
                    f[i][j] = max(f[i][j], f[last[x + j]][j] + 1)
            last[x] = i
        return max(map(max, f))

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/longest-subsequence-with-decreasing-adjacent-difference/solutions/3038930/zhuang-tai-she-ji-you-hua-pythonjavacgo-qy2bu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# TLE
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        m = max(nums)
        n = len(nums)
        f = [[-inf]*(m+2) for _ in range(m+2)]
        g = [[-inf]*(m+2) for _ in range(m+2)]
        ff = [1]*(m+2)
        gg = [1]*(m+2)
        f[nums[0]][:] = [1]*(m+2)
        g[nums[0]][:] = [1]*(m+2)

        for i in range(1,n):
            v = nums[i]
            ff[:] = [1]*(m+2)
            gg[:] = [1]*(m+2)
            # for j in range(m+2):
            #     ff[j] = gg[j] = 1
            
            for j in range(1,m+1):
                d = abs(v-j)
                ff[j] = gg[j] = max(f[j][max(0,j-d)],g[j][min(m+1,j+d)])+1
            for j in range(1,m+2):
                ff[j] = max(ff[j],ff[j-1])
            for j in range(m,0,-1):
                gg[j] = max(gg[j],gg[j+1])
            for j in range(m+2):
                f[v][j] = max(f[v][j],ff[j])
                g[v][j] = max(g[v][j],gg[j])
        ans = -inf
        for j in range(1,m+1):
            ans = max(ans,f[j][m])
        return ans 