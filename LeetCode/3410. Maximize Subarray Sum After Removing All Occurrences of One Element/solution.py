max = lambda a, b: b if b > a else a  # 手动比大小，效率更高

class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.tree = [(0, 0, 0, 0)] * (2 << n.bit_length())
        self.build(nums, 1, 0, n - 1)

    def set(self, o: int, val: int) -> None:
        self.tree[o] = (val, val, val, val)

    def merge_info(self, a: Tuple[int, int, int, int], b: Tuple[int, int, int, int]) -> Tuple[int, int, int, int]:
        ans = max(max(a[0], b[0]), a[3] + b[2])
        s = a[1] + b[1]
        pre = max(a[2], a[1] + b[2])
        suf = max(b[3], b[1] + a[3])
        return ans, s, pre, suf

    def maintain(self, o: int) -> None:
        self.tree[o] = self.merge_info(self.tree[o * 2], self.tree[o * 2 + 1])

    # 初始化线段树
    def build(self, nums, o: int, l: int, r: int) -> None:
        if l == r:
            self.set(o, nums[l])
            return
        m = (l + r) // 2
        self.build(nums, o * 2, l, m)
        self.build(nums, o * 2 + 1, m + 1, r)
        self.maintain(o)

    # 单点更新
    def update(self, o: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self.set(o, val)
            return
        m = (l + r) // 2
        if i <= m:
            self.update(o * 2, l, m, i, val)
        else:
            self.update(o * 2 + 1, m + 1, r, i, val)
        self.maintain(o)

    # 区间询问（没用到）
    def query(self, o: int, l: int, r: int, L: int, R: int) -> Tuple[int, int, int, int]:
        if L <= l and r <= R:
            return self.tree[o]
        m = (l + r) // 2
        if R <= m:
            return self.query(o * 2, l, m, L, R)
        if m < L:
            return self.query(o * 2 + 1, m + 1, r, L, R)
        return self.merge_info(
            self.query(o * 2, l, m, L, R),
            self.query(o * 2 + 1, m + 1, r, L, R)
        )

class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        t = SegmentTree(nums)
        ans = t.tree[1][0]  # 不删任何数
        if ans <= 0:
            return ans

        pos = defaultdict(list)
        for i, x in enumerate(nums):
            if x < 0:
                pos[x].append(i)
        for idx in pos.values():
            for i in idx:
                t.update(1, 0, n - 1, i, 0)  # 删除
            ans = max(ans, t.tree[1][0])
            for i in idx:
                t.update(1, 0, n - 1, i, nums[i])  # 复原
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/solutions/3039428/liang-chong-fang-fa-xian-duan-shu-qian-h-961z/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。