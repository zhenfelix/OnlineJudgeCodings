class Solution:
    def minimizeResult(self, expression: str) -> str:
        a, b = expression.split('+')
        na, nb = len(a), len(b)
        ans, exp = float('inf'), ''
        for i in range(na):
            sa = (a[:i] or '1') + '*(' + a[i:]
            ea = a[:i]+'('+a[i:]
            for j in range(nb):
                sb = b[:j+1] + ')*' + (b[j+1:] or '1')
                eb = b[:j+1]+')'+b[j+1:]
                cur = eval(sa+'+'+sb)
                if cur < ans:
                    ans = cur
                    exp = ea+'+'+eb
        # print(ans)
        return exp