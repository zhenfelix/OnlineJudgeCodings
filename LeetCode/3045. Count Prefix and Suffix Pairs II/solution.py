class Node:
    __slots__ = 'son', 'cnt'

    def __init__(self):
        self.son = dict()
        self.cnt = 0

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        root = Node()
        for t in words:
            z = self.calc_z(t)
            cur = root
            for i, c in enumerate(t):
                if c not in cur.son:
                    cur.son[c] = Node()
                cur = cur.son[c]
                if z[-1 - i] == i + 1:  # t[-1-i:] == t[:i+1]
                    ans += cur.cnt
            cur.cnt += 1
        return ans

    def calc_z(self, s: str) -> List[int]:
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(z[i - l], r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                l, r = i, i + z[i]
                z[i] += 1
        z[0] = n
        return z

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-prefix-and-suffix-pairs-ii/solutions/2644160/z-han-shu-zi-dian-shu-pythonjavacgo-by-e-5c2v/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。