PRE_SUM = [0] * 1001  # 预处理
for i in range(1, 1001):
    s = str(i * i)
    n = len(s)
    def dfs(p: int, sum: int) -> bool:
        if p == n:  # 递归终点
            return sum == i  # i 符合要求
        x = 0
        for j in range(p, n):  # 从 s[p] 到 s[j] 组成的子串
            x = x * 10 + int(s[j])  # 对应的整数值
            if dfs(j + 1, sum + x):
                return True
        return False
    PRE_SUM[i] = PRE_SUM[i - 1] + (i * i if dfs(0, 0) else 0)

class Solution:
    def punishmentNumber(self, n: int) -> int:
        return PRE_SUM[n]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-the-punishment-number-of-an-integer/solutions/2277792/yu-chu-li-hui-su-by-endlesscheng-ro3s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def punishmentNumber(self, n: int) -> int:
        @lru_cache(None)
        def dfs(v,nums,i):
            # print(v,nums,i)
            if v < 0:
                return False
            if i == len(nums):
                return v == 0
            for j in range(i,len(nums)):
                if dfs(v-int(nums[i:j+1]),nums,j+1):
                    return True
            return False
        
        ans = 0
        for x in range(1,n+1):
            if dfs(x,str(x*x),0):
                ans += x*x
        return ans 