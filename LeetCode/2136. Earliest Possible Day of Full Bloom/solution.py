# class Solution:
#     def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
#         sums = sum(plantTime)
#         n = len(plantTime)
#         idx = [i for i in range(n)]
#         idx.sort(key = lambda i: growTime[i])
#         def check(x):
#             cur = sums
#             i = 0
#             pq = []
#             while i < n:
#                 while i < n and cur+growTime[idx[i]] <= x:
#                     heapq.heappush(pq, -plantTime[idx[i]])
#                     i += 1
#                 if not pq:
#                     return False
#                 delta = heapq.heappop(pq)
#                 cur += delta
#             return True

#         lo, hi = sums+min(growTime), sums+max(growTime)
#         while lo <= hi:
#             mid = (lo+hi)//2
#             if check(mid):
#                 hi = mid-1
#             else:
#                 lo = mid+1
#         return lo


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        a = list(zip(plantTime, growTime))
        a.sort(key=lambda x: -x[1])
        ans, day = 0, 0
        for p in a:
            day += p[0]
            ans = max(ans, day + p[1])
        return ans


# 作者：endlesscheng
# 链接：https://leetcode-cn.com/problems/earliest-possible-day-of-full-bloom/solution/tan-xin-ji-qi-zheng-ming-by-endlesscheng-hfwe/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。