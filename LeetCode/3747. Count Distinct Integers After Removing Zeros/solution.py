class Solution:
    def countDistinct(self, s: int) -> int:
        m = s 
        s = list(map(int,list(str(s))))
        n = len(s)
        @lru_cache(None)
        def dfs(i,first,flag,limit):
            if i == n:
                return flag
            up = 10
            if limit:
                up = s[i]+1
            ans = 0
            for ch in range(up):
                ans += dfs(i+1, first and ch == 0, flag or (not first and ch == 0), limit and ch == s[i])
            return ans
        return m-dfs(0,True,False,True)

class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        m = len(s)

        # 计算长度小于 m 的不含 0 的整数个数
        # 9^1 + 9^2 + ... + 9^(m-1) = (9^m - 9) / 8
        pow9 = 9 ** m
        ans = (pow9 - 9) // 8

        # 计算长度恰好等于 m 的不含 0 的整数个数
        for i, d in enumerate(s):
            if d == '0':  # 只能填 0，不合法，跳出循环
                break
            # 这一位填 1 到 d-1，后面的数位可以随便填 1 到 9
            v = int(d) - 1
            if i == m - 1:
                v += 1  # 最低位可以等于 d
            pow9 //= 9
            ans += v * pow9
            # 然后，这一位填 d，继续遍历

        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-distinct-integers-after-removing-zeros/solutions/3832951/tong-ji-bu-han-0-de-zheng-shu-ge-shu-pyt-6pun/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。