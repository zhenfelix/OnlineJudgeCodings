# class Solution:
#     def makeStringSorted(self, s: str) -> int:
#         cnt, MOD = 0, 10**9+7
#         cc = Counter(s)

#         def quickmul(a, q):
#             res = 1
#             while q:
#                 if q & 1:
#                     res *= a
#                     res %= MOD
#                 a *= a
#                 a %= MOD
#                 q = (q >> 1)
#             return res

#         factor = [1]*(len(s)+1)
#         for i in range(1, len(factor)):
#             factor[i] = i*factor[i-1] % MOD
#         rfactor = []
#         for f in factor:
#             rfactor.append(quickmul(f, MOD-2))

#         def calc():
#             total, sums = 1, 0
#             for k, v in cc.items():
#                 sums += v
#                 total *= rfactor[v]
#                 total %= MOD
#             total *= factor[sums]
#             total %= MOD
#             return total

#         for ch in s:
#             cur = 'a'
#             while cur < ch:
#                 if cc[cur] > 0:
#                     cc[cur] -= 1
#                     cnt += calc()
#                     cnt %= MOD
#                     cc[cur] += 1
#                 cur = chr(ord(cur)+1)
#             cc[ch] -= 1
#         return cnt


class Solution:
    def makeStringSorted(self, s: str) -> int:
        cnt, MOD = 0, 10**9+7
        cc = Counter(s)

        def quickmul(a, q):
            res = 1
            while q:
                if q & 1:
                    res *= a
                    res %= MOD
                a *= a
                a %= MOD
                q = (q >> 1)
            return res

        factor = [1]*(len(s)+1)
        for i in range(1, len(factor)):
            factor[i] = i*factor[i-1] % MOD
        rfactor = []
        for f in factor:
            rfactor.append(quickmul(f, MOD-2))

        def calc(ch):
            total, sums, less = 1, 0, 0
            for k, v in cc.items():
                if k < ch:
                    less += v
                sums += v
                total *= rfactor[v]
                total %= MOD
            total *= factor[sums-1]
            total *= less
            total %= MOD
            return total

        for ch in s:
            cnt += calc(ch)
            cnt %= MOD
            cc[ch] -= 1
        return cnt