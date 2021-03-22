class Solution:
    def maxValue(self, n, index, maxSum):
        def test(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) // 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) // 2
            return res - a

        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1        


# class Solution:
#     def maxValue(self, n: int, index: int, maxSum: int) -> int:
#         def calc(x):
#             # print(x)
#             sums = n 
#             x = max(0,x-1)
#             left = max(0,x-index)
#             sums += (left+x)*(min(index+1,x+1))//2
#             # print(x,sums)
#             right = max(0,x-(n-index-1))
#             sums += (right+x)*(min(n-index,x+1))//2
#             # print(x,sums)
#             sums -= x 
#             return sums

#         lo, hi = 0, maxSum
#         while lo <= hi:
#             mid = (lo+hi)//2
#             tmp = calc(mid)
#             # print(mid,tmp)
#             if tmp > maxSum:
#                 hi = mid - 1
#             else:
#                 lo = mid + 1
#         return hi