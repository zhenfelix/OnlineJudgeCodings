class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        idx = sorted(range(n), key=lambda i: nums[i])

        # rank[i] 表示 nums[i] 是 nums 中的第几小，或者说节点 i 在 idx 中的下标
        rank = [0] * n
        for i, j in enumerate(idx):
            rank[j] = i

        # 双指针，从第 i 小的数开始，向左一步，最远能跳到第 left 小的数
        mx = n.bit_length()
        pa = [[0] * mx for _ in range(n)]
        left = 0
        for i, j in enumerate(idx):
            while nums[j] - nums[idx[left]] > maxDiff:
                left += 1
            pa[i][0] = left

        # 倍增
        for i in range(mx - 1):
            for x in range(n):
                p = pa[x][i]
                pa[x][i + 1] = pa[p][i]

        ans = []
        for l, r in queries:
            if l == r:  # 不用跳
                ans.append(0)
                continue
            l, r = rank[l], rank[r]
            if l > r:  # 保证 l 在 r 左边
                l, r = r, l
            # 从 r 开始，向左跳到 l
            res = 0
            for k in range(mx - 1, -1, -1):
                if pa[r][k] > l:
                    res |= 1 << k
                    r = pa[r][k]
            ans.append(-1 if pa[r][0] > l else res + 1)  # 再跳一步就能到 l
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/path-existence-queries-in-a-graph-ii/solutions/3663266/pai-xu-shuang-zhi-zhen-bei-zeng-pythonja-ckht/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。