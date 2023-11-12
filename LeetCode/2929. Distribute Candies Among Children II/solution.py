class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > limit*3: return 0
        hi = n-max(0,n-2*limit)
        lo = max(0,n-limit)
        def calc(x):
            return min(limit,x)-max(0,x-limit)+1
        def calc2(mi,mx):
            return (mi+mx)*(mx-mi+1)//2
        # print(lo,hi)
        if hi <= limit:
            return calc2(calc(lo),calc(hi))
        elif lo >= limit:
            return calc2(calc(hi),calc(lo))
        else:
            return calc2(calc(lo),calc(limit))+calc2(calc(hi),calc(limit))-limit-1


def c2(n: int) -> int:
    return n * (n - 1) // 2 if n > 1 else 0

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return c2(n + 2) - 3 * c2(n - limit + 1) + 3 * c2(n - 2 * limit) - c2(n - 3 * limit - 1)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/distribute-candies-among-children-ii/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。