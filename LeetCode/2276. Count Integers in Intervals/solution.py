class CountIntervals:
    __slots__ = ('left', 'right', 'l', 'r', 'cnt')

    def __init__(self, l=1, r=10 ** 9):
        self.left = self.right = None
        self.l, self.r, self.cnt = l, r, 0

    def add(self, l: int, r: int) -> None:
        if self.cnt == self.r - self.l + 1: return  # self 已被完整覆盖，无需执行任何操作
        if l <= self.l and self.r <= r:  # self 已被区间 [l,r] 完整覆盖，不再继续递归
            self.cnt = self.r - self.l + 1
            return
        mid = (self.l + self.r) // 2
        if self.left is None: self.left = CountIntervals(self.l, mid)  # 动态开点
        if self.right is None: self.right = CountIntervals(mid + 1, self.r)  # 动态开点
        if l <= mid: self.left.add(l, r)
        if mid < r: self.right.add(l, r)
        self.cnt = self.left.cnt + self.right.cnt

    def count(self) -> int:
        return self.cnt


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/count-integers-in-intervals/solution/by-endlesscheng-clk2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



from sortedcontainers import * 
class CountIntervals:

    def __init__(self):

        self.sl = SortedList([inf])
        self.mp = {inf:inf}
        self.sz = 0


    def add(self, left: int, right: int) -> None:
        idx = self.sl.bisect_left(left)
        n = len(self.sl)
        for i in range(idx,n):
            if self.mp[self.sl[i]] > right:
                del self.sl[idx:i]
                break
            r = self.sl[i]
            l = self.mp[r]
            self.sz -= (r-l+1)
            right = max(right,r)
            left = min(left,l)
        self.sl.add(right)
        self.mp[right] = left
        self.sz += (right-left+1)
        # print(self.sl)


    def count(self) -> int:
        return self.sz



# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()