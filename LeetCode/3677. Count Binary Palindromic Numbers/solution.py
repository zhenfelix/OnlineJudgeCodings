class Solution:
    def countBinaryPalindromes(self, M: int) -> int:
        s = list(map(int,list(bin(M)[2:])))
        n = len(s)


        @lru_cache(None)
        def dfs(i,j,pre,limit,tail):
            if i > j:
                return 0 if limit and tail else 1
            mx = 1
            if limit:
                mx = s[i]
            ans = 0
            for v in range(mx+1):
                ans += dfs(i+1,j-(pre|v),pre|v,limit&(v==s[i]),(v>=s[j])&(tail|(v>s[j])))
            # print(i,j,pre,limit,tail)
            # print(ans)
            return ans 
        return dfs(0,n-1,0,1,0)


class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1

        m = n.bit_length()  # n 的二进制长度

        # 对于二进制长度小于 m 的回文数，左半边随便填
        ans = 1  # 0 也是回文数
        # 枚举二进制长度，最高位填 1，回文数左半的其余位置随便填
        for i in range(1, m):
            ans += 1 << ((i - 1) // 2)

        # 最高位一定是 1，从次高位开始填
        for i in range(m - 2, m // 2 - 1, -1):
            if n >> i & 1:
                # 这一位可以填 0，那么回文数左半的剩余位置可以随便填
                ans += 1 << (i - m // 2)
            # 在后续循环中，这一位填 1

        pal = n >> (m // 2)
        # 左半反转到右半
        # 如果 m 是奇数，那么去掉回文中心再反转
        v = pal >> (m % 2)
        while v:
            pal = pal * 2 + v % 2
            v //= 2
        if pal <= n:
            ans += 1

        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-binary-palindromic-numbers/solutions/3774534/olog-n-zuo-fa-pythonjavacgo-by-endlessch-1ggp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

好的，我们来深入解析第三部分的代码。

### 第三部分的目标

在解释代码之前，我们先明确这一步的**上下文和目标**。

  * **第一部分**已经计算了所有二进制长度**小于** `n` 的回文数。
  * **第二部分**已经计算了所有二进制长度**等于** `n`，但在某个高位上就已经**小于** `n` 的回文数。

那么，还剩下哪一种可能的回文数没有被计算呢？

只剩下一种：**一个长度与 `n` 相同，且其整个“前半部分”与 `n` 的“前半部分”完全相同的回文数**。

第三部分代码的目标就是：

1.  根据 `n` 的前半部分，精确地**构造**出这最后一个候选的回文数。
2.  **检查**这个构造出来的数是否真的小于或等于 `n`。如果是，就将其计入总数。

