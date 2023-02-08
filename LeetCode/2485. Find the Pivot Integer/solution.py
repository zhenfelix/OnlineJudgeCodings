class Solution:
    def pivotInteger(self, n: int) -> int:
        m = n * (n + 1) // 2
        x = int(m ** 0.5)
        return x if x * x == m else -1

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-the-pivot-integer/solutions/1993442/o1-zuo-fa-by-endlesscheng-571j/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def pivotInteger(self, n: int) -> int:
        for x in range(1,n+1):
            if (1+x)*x == (x+n)*(n-x+1):
                return x  
        return -1