# 手写 min 更快
min = lambda a, b: b if b < a else a

class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        u = 1 << len(lists)
        sorted_ = [[] for _ in range(u)]
        for i, a in enumerate(lists):  # 枚举不在 s 中的下标 i
            high_bit = 1 << i
            for s in range(high_bit):
                b = sorted_[s] + a
                b.sort()  # 线性合并的写法见另一份代码【Python3 写法二】
                sorted_[high_bit | s] = b

        f = [inf] * u
        for i in range(1, u):
            if i & (i - 1) == 0:  # i 只包含一个元素，无法分解成两个非空子集
                f[i] = 0
                continue
            # 枚举 i 的非空真子集 j
            j = i & (i - 1)
            while j > (i ^ j):
                k = i ^ j  # j 关于 i 的补集是 k
                med_j = sorted_[j][(len(sorted_[j]) - 1) // 2]
                med_k = sorted_[k][(len(sorted_[k]) - 1) // 2]
                f[i] = min(f[i], f[j] + f[k] + abs(med_j - med_k))
                j = (j - 1) & i
            f[i] += len(sorted_[i])

        return f[-1]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-cost-to-merge-sorted-lists/solutions/3872282/yu-chu-li-zi-ji-zhuang-ya-dppythonjavacg-isio/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。