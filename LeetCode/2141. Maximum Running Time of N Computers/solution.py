# class Solution:
#     def maxRunTime(self, n: int, batteries: List[int]) -> int:
#         lo, hi = min(batteries), sum(batteries)//n 
#         m = len(batteries)
#         batteries.sort()
#         # print(batteries)
#         while lo <= hi:
#             mid = (lo+hi)//2
#             cur = 0
#             for i in range(m):
#                 if batteries[i] <= mid:
#                     cur += batteries[i]
#                 else:
#                     cur += mid

#             if cur >= mid*n:
#                 lo = mid + 1
#             else:
#                 hi = mid - 1
#         return hi




# class Solution:
#     def maxRunTime(self, n: int, batteries: List[int]) -> int:
#         lo, hi = min(batteries), sum(batteries)//n 
#         m = len(batteries)
#         batteries.sort()
#         sums = [0]
#         for i in range(m):
#             sums.append(sums[-1]+batteries[i])
#         # print(batteries)
#         while lo <= hi:
#             mid = (lo+hi)//2
#             idx = bisect.bisect_right(batteries,mid)

#             if sums[idx]+mid*(m-idx) >= mid*n:
#                 lo = mid + 1
#             else:
#                 hi = mid - 1
#         return hi

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)
        tot = sum(batteries)
        for b in batteries:
            if b <= tot//n:
                return tot//n 
            tot -= b 
            n -= 1
        return 0


