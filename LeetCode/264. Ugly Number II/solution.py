# import math

# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         dp = [1,2,3,4,5]
#         if n < 6:
#             return dp[n-1]
#         for i in range(5,n):
#             left, right = 0, i-1
#             num = math.inf
#             while left <= right:
#                 if dp[left]*dp[right] <= dp[-1]:
#                     left += 1
#                 elif dp[left]*dp[right] < num:
#                     num = dp[left]*dp[right]
#                     right -= 1
#                 else:
#                     right -= 1
#             dp.append(num)
#         return dp[-1]


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/ugly-number-ii/solution/chou-shu-ii-by-leetcode-solution-uoqd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


import math

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
       
        i, j, k = 0, 0, 0
        for idx in range(1,n):
            while dp[i]*2 <= dp[-1]:
                i += 1
            while dp[j]*3 <= dp[-1]:
                j += 1
            while dp[k]*5 <= dp[-1]:
                k += 1
            
            dp.append(min(dp[i]*2,dp[j]*3,dp[k]*5))
        # print(dp)
        return dp[-1]


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q = [(2,2,0),(3,3,0),(5,5,0)]
        arr = [1]
        while len(arr) < n:
            cur, m, i = heapq.heappop(q)
            if cur > arr[-1]:
                arr.append(cur)
            i += 1
            # print(arr,i,m)
            while arr[i]*m <= arr[-1]:
                i += 1
            heapq.heappush(q,(arr[i]*m,m,i))
        return arr[-1]