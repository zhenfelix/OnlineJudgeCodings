class Node:
    __slots__ = 'children', 'cnt'

    def __init__(self):
        self.children = [None, None]
        self.cnt = 0  # 子树大小

class Trie:
    HIGH_BIT = 19

    def __init__(self):
        self.root = Node()

    # 添加 val
    def insert(self, val: int) -> None:
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            if cur.children[bit] is None:
                cur.children[bit] = Node()
            cur = cur.children[bit]
            cur.cnt += 1  # 维护子树大小
        return cur

    # （懒惰）删除 val
    # 要求 val 必须在 trie 中
    def remove(self, val: int) -> None:
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            cur = cur.children[(val >> i) & 1]
            cur.cnt -= 1  # 维护子树大小
        return cur

    # 返回 val 与 trie 中一个元素的最大异或和
    # 要求 trie 中至少有一个元素
    def max_xor(self, val: int) -> int:
        cur = self.root
        ans = 0
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            # 如果 cur.children[bit^1].cnt == 0，视作空节点
            if cur.children[bit ^ 1] and cur.children[bit ^ 1].cnt:
                ans |= 1 << i
                bit ^= 1
            cur = cur.children[bit]
        return ans

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        t = Trie()
        ans = left = 0
        for y in nums:
            t.insert(y)
            while nums[left] * 2 < y:
                t.remove(nums[left])
                left += 1
            ans = max(ans, t.max_xor(y))
        return ans


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/2g47c7/view/AstFlr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Node:
    def __init__(self):
        self.cnt = 0
        self.child = dict()


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        mx = 25
        root = Node()
        def update(x, delta):
            cur = root
            cur.cnt += delta
            for i in range(mx)[::-1]:
                ch = (x>>i)&1
                if ch not in cur.child:
                    cur.child[ch] = Node()
                cur = cur.child[ch]
                cur.cnt += delta
            return 
        nums.sort()
        n = len(nums)
        ans = 0
        j = 0
        for i in range(n):
            while j < n and nums[j]-nums[i] <= nums[i]:
                update(nums[j],1)
                j += 1
            v = 0
            x = nums[i]
            cur = root
            for i in range(mx)[::-1]:
                ch = (x>>i)&1
                if (ch^1) in cur.child and cur.child[ch^1].cnt > 0:
                    v |= (1<<i)
                    cur = cur.child[ch^1]
                else:
                    cur = cur.child[ch]
            ans = max(ans,v)
            update(x,-1)
        return ans 