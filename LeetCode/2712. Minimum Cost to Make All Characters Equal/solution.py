class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1, n):
            if s[i] != s[i-1]:
                ans += min(i, n-i)
        return ans


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/5eR2p8/view/wgt6tJ/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        left = [[inf]*n for _ in range(2)]
        v = int(s[0])
        left[v][0] = 0
        left[1-v][0] = 1
        for i in range(1,n):
            u = int(s[i])
            left[u][i] = left[u][i-1]
            left[1-u][i] = left[u][i-1]+i+1
        right = [[inf]*n for _ in range(2)]
        v = int(s[-1])
        right[v][-1] = 0
        right[1-v][-1] = 1
        for i in range(n-1)[::-1]:
            u = int(s[i])
            right[u][i] = right[u][i+1]
            right[1-u][i] = right[u][i+1]+n-i
        ans = inf 
        ans = min(ans,min(left[0][-1],left[1][-1]))
        ans = min(ans,min(right[0][0],right[1][0]))
        for i in range(n-1):
            ans = min(ans,min(left[0][i]+right[0][i+1],left[1][i]+right[1][i+1]))
        return ans 