class Solution:
    def minRecSize(self, lines: List[List[int]]) -> float:
        if len(lines) == 2 or all(lines[0][0] == x for x, _ in lines):
            return 0
        n = len(lines)
        delta = 10**(-8)

        def judge(kb, x, is_reverse):
            if is_reverse:
                # mp = {}
                # for k, b in kb:
                #     mp[k] = k*x+b
                # ky = list(mp.items())
                # for i in range(1, len(ky)):
                #     if ky[i][1] > ky[i-1][1]:
                #         return False

                for i in range(1,n):
                    if kb[i][0] > kb[i-1][0] + delta and kb[i][0]*x+kb[i][1] > kb[i-1][0]*x+kb[i-1][1] + delta:
                        return False
                return True
            else:
                # mp = {}
                # for k, b in kb[::-1]:
                #     mp[k] = k*x+b
                # ky = list(mp.items())
                # for i in range(1, len(ky)):
                #     if ky[i][1] < ky[i-1][1]:
                #         return True
                for i in range(1,n):
                    if kb[i][0] > kb[i-1][0] + delta and kb[i][0]*x+kb[i][1] + delta < kb[i-1][0]*x+kb[i-1][1]:
                        return True
                return False

        def func(kb, is_reverse):
            lo, hi = -10**10, 10**10
            while hi-lo > 10**(-6):
                mid = (lo+hi)/2
                # print(mid)
                if judge(kb, mid, is_reverse):
                    lo = mid
                else:
                    hi = mid
            return mid

        xkb = sorted([[k, b] for k, b in lines])
        ykb = sorted([[1/k, -b/k] for k, b in lines])
        left = func(sorted(xkb, key=lambda xx: (xx[0], -xx[1])), True)
        right = func(xkb, False)
        bottom = func(sorted(ykb, key=lambda xx: (xx[0], -xx[1])), True)
        up = func(ykb, False)
        # print(left, right, bottom, up)
        return abs((right-left)*(up-bottom))

