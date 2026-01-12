from typing import List

# 1. 定义线段树节点
class Node:
    def __init__(self, l, r, count=0, pre=0, suf=0, total=0):
        self.l = l               # 区间左端点
        self.r = r               # 区间右端点
        self.count = count       # [l,r] 内的稳定子数组总数
        self.prefix_len = pre    # [l,r] 的最长稳定前缀长度
        self.suffix_len = suf    # [l,r] 的最长稳定后缀长度
        self.total_len = total   # 区间总长 (r - l + 1)
        self.left = None         # 左子节点
        self.right = None        # 右子节点

class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        self.nums = nums
        n = len(nums)
        # 3. 定义单位元节点 (用于查询时不相交的情况)
        self.identity = Node(-1, -1, 0, 0, 0, 0)
        
        # 4. 构建线段树
        self.root = self._build(0, n - 1)
        
        # 7. 处理所有查询
        ans = []
        for l, r in queries:
            result_node = self._query(self.root, l, r)
            ans.append(result_node.count)
        return ans

    # 2. 定义合并逻辑
    def _merge(self, left: Node, right: Node) -> Node:
        # 处理单位元节点
        if left.total_len == 0:
            return right
        if right.total_len == 0:
            return left
            
        # 合并两个子节点
        merged = Node(left.l, right.r)
        merged.total_len = left.total_len + right.total_len
        merged.count = left.count + right.count
        merged.prefix_len = left.prefix_len
        merged.suffix_len = right.suffix_len
        
        # 检查中点连接处是否稳定
        mid = left.r
        if self.nums[mid] <= self.nums[mid + 1]:
            # 2a. 增加跨中点的稳定子数组数量
            merged.count += left.suffix_len * right.prefix_len
            
            # 2b. 更新合并后的前缀长
            if left.prefix_len == left.total_len:
                merged.prefix_len = left.total_len + right.prefix_len
            
            # 2c. 更新合并后的后缀长
            if right.suffix_len == right.total_len:
                merged.suffix_len = right.total_len + left.suffix_len
                
        return merged

    # 5. 定义构建逻辑
    def _build(self, l: int, r: int) -> Node:
        # 叶子节点 (单个元素)
        if l == r:
            # count=1 ([nums[l]])
            # pre=1, suf=1, total=1
            return Node(l, r, count=1, pre=1, suf=1, total=1)
        
        mid = (l + r) // 2
        left_child = self._build(l, mid)
        right_child = self._build(mid + 1, r)
        
        # 递归合并
        merged_node = self._merge(left_child, right_child)
        merged_node.left = left_child
        merged_node.right = right_child
        
        return merged_node

    # 6. 定义查询逻辑
    def _query(self, node: Node, L: int, R: int) -> Node:
        # [L, R] 是查询区间
        # [node.l, node.r] 是当前节点区间
        
        # 1. 完全不相交: 返回单位元
        if node.r < L or node.l > R:
            return self.identity
            
        # 2. 完全包含: 返回当前节点
        if L <= node.l and node.r <= R:
            return node
            
        # 3. 部分相交: 递归查询左右子树，并合并结果
        left_result = self._query(node.left, L, R)
        right_result = self._query(node.right, L, R)
        
        return self._merge(left_result, right_result)



class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # 找递增段
        left = []  # 递增段的左端点
        s = [0]  # 递增子数组个数的前缀和
        start = 0
        for i, x in enumerate(nums):
            if i == n - 1 or x > nums[i + 1]:
                # 找到了一个递增段 [start, i]
                left.append(start)
                m = i - start + 1
                # 长为 m 的子数组中有 m*(m+1)/2 个递增子数组
                # 计算 m*(m+1)/2 的前缀和
                s.append(s[-1] + m * (m + 1) // 2)
                start = i + 1  # 下一个递增段的左端点

        ans = []
        for l, r in queries:
            i = bisect_right(left, l)  # 左端点严格大于 l 的第一个区间
            j = bisect_right(left, r) - 1  # 包含 r 的最后一个区间

            # l 和 r 在同一个区间
            if i > j:
                m = r - l + 1
                ans.append(m * (m + 1) // 2)
                continue

            # l 和 r 在不同区间
            # 分成三段 [l, left[i]) + [left[i], left[j]) + [left[j], r]
            # 中间那段的子数组个数用前缀和计算
            m = left[i] - l
            m2 = r - left[j] + 1
            ans.append(m * (m + 1) // 2 + (s[j] - s[i]) + m2 * (m2 + 1) // 2)
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-stable-subarrays/solutions/3832945/fen-duan-er-fen-cha-zhao-qian-zhui-he-py-ukgs/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。