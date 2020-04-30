class Solution(object):
    def findMinFibonacciNumbers(self, k):
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])

        ans = 0
        while k:
            x = fib.pop()
            if k >= x:
                k -= x
                ans += 1
        return ans

Zeckendorf representation (ZR) of K (a representation of K as a sum of non-adjacent Fibonacci values)

https://discordapp.com/channels/612060087900438538/612587060099940372/701101422241906729

# class Solution:
#     def findMinFibonacciNumbers(self, k: int) -> int:
#         fib = [1,1]
#         while fib[-1] < k:
#             fib.append(fib[-1]+fib[-2])
#         # print(fib)
#         step = 0
#         while k > 0:
#             idx = bisect.bisect_right(fib,k)-1
#             k -= fib[idx]
#             step += 1
#         return step