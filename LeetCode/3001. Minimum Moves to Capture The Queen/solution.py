class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        def ok(l: int, m: int, r: int) -> bool:
            return not min(l, r) < m < max(l, r)

        if a == e and (c != e or ok(b, d, f)) or \
           b == f and (d != f or ok(a, c, e)) or \
           c + d == e + f and (a + b != e + f or ok(c, a, e)) or \
           c - d == e - f and (a - b != e - f or ok(c, a, e)):
            return 1
        return 2

作者：灵茶山艾府
链接：https://leetcode.cn/problems/minimum-moves-to-capture-the-queen/solutions/2594432/fen-lei-tao-lun-jian-ji-xie-fa-pythonjav-aoa8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。