class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cc1, cc2 = Counter(s), Counter(t)
        cnt = 0
        for i in range(26):
            ch = chr(ord('a')+i)
            cnt += abs(cc1[ch]-cc2[ch])
        return cnt


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs = collections.Counter(s)
        ct = collections.Counter(t)
        return sum(abs(cs[ch] - ct[ch]) for ch in set(cs.keys()) | set(ct.keys()))


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/eU8bPl/view/rUilTq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。