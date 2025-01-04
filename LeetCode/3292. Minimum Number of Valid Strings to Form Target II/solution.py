class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)

        # 多项式字符串哈希（方便计算子串哈希值）
        # 哈希函数 hash(s) = s[0] * BASE^(n-1) + s[1] * BASE^(n-2) + ... + s[n-2] * BASE + s[n-1]
        MOD = 1_070_777_777
        BASE = randint(8 * 10 ** 8, 9 * 10 ** 8)  # 随机 BASE，防止 hack
        pow_base = [1] + [0] * n  # pow_base[i] = BASE^i
        pre_hash = [0] * (n + 1)  # 前缀哈希值 pre_hash[i] = hash(s[:i])
        for i, b in enumerate(target):
            pow_base[i + 1] = pow_base[i] * BASE % MOD
            pre_hash[i + 1] = (pre_hash[i] * BASE + ord(b)) % MOD  # 秦九韶算法计算多项式哈希

        # 计算子串 target[l:r] 的哈希值，注意这是左闭右开区间 [l,r)
        # 计算方法类似前缀和
        def sub_hash(l: int, r: int) -> int:
            return (pre_hash[r] - pre_hash[l] * pow_base[r - l]) % MOD

        # 保存每个 words[i] 的每个前缀的哈希值，按照长度分组
        max_len = max(map(len, words))
        sets = [set() for _ in range(max_len)]
        for w in words:
            h = 0
            for j, b in enumerate(w):
                h = (h * BASE + ord(b)) % MOD
                sets[j].add(h)  # 注意 j 从 0 开始

        ans = 0
        cur_r = 0  # 已建造的桥的右端点
        nxt_r = 0  # 下一座桥的右端点的最大值
        for i in range(n):
            check = lambda sz: sub_hash(i, i + sz + 1) not in sets[sz]
            sz = bisect_left(range(min(n - i, max_len)), True, key=check)
            nxt_r = max(nxt_r, i + sz)
            if i == cur_r:  # 到达已建造的桥的右端点
                if i == nxt_r:  # 无论怎么造桥，都无法从 i 到 i+1
                    return -1
                cur_r = nxt_r  # 建造下一座桥
                ans += 1
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/solutions/2917929/ac-zi-dong-ji-pythonjavacgo-by-endlessch-hcqk/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 从根到 node 的字符串是某个（某些）words[i] 的前缀
class Node:
    __slots__ = 'son', 'fail', 'len'

    def __init__(self, len=0):
        self.son = [None] * 26
        self.fail = None  # 当 cur.son[i] 不能匹配 target 中的某个字符时，cur.fail.son[i] 即为下一个待匹配节点（等于 root 则表示没有匹配）
        self.len = len  # 从根到 node 的字符串的长度，也是 node 在 trie 中的深度

class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def put(self, s: str) -> None:
        cur = self.root
        for b in s:
            b = ord(b) - ord('a')
            if cur.son[b] is None:
                cur.son[b] = Node(cur.len + 1)
            cur = cur.son[b]

    def build_fail(self) -> None:
        self.root.fail = self.root
        q = deque()
        for i, son in enumerate(self.root.son):
            if son is None:
                self.root.son[i] = self.root
            else:
                son.fail = self.root  # 第一层的失配指针，都指向根节点 ∅
                q.append(son)
        # BFS
        while q:
            cur = q.popleft()
            for i, son in enumerate(cur.son):
                if son is None:
                    # 虚拟子节点 cur.son[i]，和 cur.fail.son[i] 是同一个
                    # 方便失配时直接跳到下一个可能匹配的位置（但不一定是某个 words[k] 的最后一个字母）
                    cur.son[i] = cur.fail.son[i]
                    continue
                son.fail = cur.fail.son[i]  # 计算失配位置
                q.append(son)

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        ac = AhoCorasick()
        for w in words:
            ac.put(w)
        ac.build_fail()

        n = len(target)
        f = [0] * (n + 1)
        cur = root = ac.root
        for i, c in enumerate(target, 1):
            # 如果没有匹配相当于移动到 fail 的 son[c]
            cur = cur.son[ord(c) - ord('a')]
            # 没有任何字符串的前缀与 target[..i] 的后缀匹配
            if cur is root:
                return -1
            f[i] = f[i - cur.len] + 1
        return f[n]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/solutions/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。