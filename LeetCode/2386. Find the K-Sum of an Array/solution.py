# [Amazon SDE New Grad | OA | k most popular combos](https://leetcode.com/discuss/interview-question/1895396/amazon-sde-new-grad-oa-k-most-popular-combos)
# [Find k-th minimum sum of every possible subset](https://stackoverflow.com/questions/33219712/find-k-th-minimum-sum-of-every-possible-subset/33220735#33220735)

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        sum = tot = 0
        for i, x in enumerate(nums):
            if x >= 0:
                sum += x
                tot += x
            else:
                tot -= x
                nums[i] = -x
        nums.sort()

        def count(limit: int) -> int:
            cnt = 0
            def f(i: int, s: int) -> None:
                nonlocal cnt
                if i == len(nums) or cnt >= k - 1 or s + nums[i] > limit:
                    return
                cnt += 1
                f(i + 1, s + nums[i])  # 选
                f(i + 1, s)  # 不选
            f(0, 0)
            return cnt
        return sum - bisect_left(range(tot), k - 1, key=count)


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/find-the-k-sum-of-an-array/solution/zhuan-huan-dui-by-endlesscheng-8yiq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 二分
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        s, tot = 0, 0
        arr = []
        for x in nums:
            if x < 0:
                s -= x
                x = -x
            arr.append(x)
            tot += x 
        arr.sort()
        n = len(arr)
        def check(limit):
            cnt = 1
            if cnt > k-1:
                return False
            m = min(k,n)
            q = [(0,0)]
            while q:
                nq = []
                for start, sums in q:
                    for i in range(start,m):
                        if sums+arr[i] > limit:
                            break
                        nq.append((i+1,sums+arr[i]))
                        cnt += 1
                        if cnt > k-1:
                            return False
                q = nq 
            return True 

        def kthSmallest():
            lo, hi = 0, tot
            while lo <= hi:
                mid = (lo+hi)//2
                if check(mid):
                    lo = mid+1
                else:
                    hi = mid-1
            # print(lo)
            return lo
        return tot-kthSmallest()-s

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        s, tot = 0, 0
        arr = []
        for x in nums:
            if x < 0:
                s -= x
                x = -x
            arr.append(x)
            tot += x 
        arr.sort()
        n = len(arr)
        def kthSmallest():
            if k == 1:
                return 0
            hq = [(arr[0],0)]
            res = 0
            for _ in range(1,k):
                cur, idx = heapq.heappop(hq)
                res = cur
                if idx+1 < n:
                    heapq.heappush(hq,(cur+arr[idx+1],idx+1))
                    heapq.heappush(hq,(cur+arr[idx+1]-arr[idx],idx+1))
            return res
        return tot-kthSmallest()-s


# TLE
# class Solution:
#     def kSum(self, nums: List[int], k: int) -> int:
#         nums.sort(reverse=True)
#         dp = [0]
#         delta = 0
#         for cur in nums:
#             m = len(dp)
#             if m > k and cur > 0:
#                 delta += cur
#                 continue
#             for i in range(m):
#                 dp.append(dp[i]+cur)
#             dp.sort(reverse=True)
#         print(dp,delta)
#         return dp[k-1]+delta
