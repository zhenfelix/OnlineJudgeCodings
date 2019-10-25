# class Solution:
#     def findKthNumber(self, n: int, k: int) -> int:
#         def nxt(digits):
#             cur = 1
#             while True:
#                 if cur < digits:
#                     if cur*10 <= n:
#                         cur *= 10
#                     else:
#                         cur += 1
#                         while cur%10 == 0:
#                             cur //= 10
#                 else:
#                     cur += 1
#                     if cur > n:
#                         cur -= 1
#                         cur //= 10
#                         cur += 1
#                     while cur%10 == 0:
#                         cur //= 10
#                 yield cur

#         digits_ = 1
#         while n//digits_ > 0:
#             digits_ *= 10
#         digits_ //= 10
#         generator = nxt(digits_)
#         res = 1
#         # for i in generator:
#         #     print(i)
#         for i in range(1,k):
#             res = next(generator)
#         return res


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        while k > 1:
            steps = self.calsteps(cur, n)
            if steps < k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur

    def calsteps(self, n1, n):
        steps = 0
        n2 = n1 + 1
        while n1 <= n:
            steps += min(n+1,n2) - n1
            n1 *= 10
            n2 *= 10
        return steps
