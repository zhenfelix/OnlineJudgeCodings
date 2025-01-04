class Solution:
    def waysToReachStair(self, k: int) -> int:
        # 2 ^ 0 + 2 ^ 1 + ... + 2 ^ (j - 1) - v
        # v <= j + 1
        k -= 1
        ans = 0
        for j in range(35):
            tot = (1 << j) - 1
            if tot - j - 1 <= k <= tot:
                ans += math.comb(j + 1, tot - k)
        return ans


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/GKQ9WA/view/voCYUT/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def waysToReachStair(self, k: int) -> int:
        mx = 32
        @lru_cache(None)
        def dfs(cur,j,ok):
            if cur < 0: return 0
            if cur > (1<<j): return 0
            if cur == 1: 
                if j == 0: return 1
            if j < 0: return 0
            ans = 0
            if ok:
                ans += dfs(cur+1,j,False)
            if j > 0:
                ans += dfs(cur-(1<<(j-1)),j-1,True)
            return ans 
        return sum(dfs(k,i,True) for i in range(mx))