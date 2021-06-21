# class Solution:
#     def minDifference(self, nums, queries):
#         N, ans, dp = max(nums), [], [[0]*(max(nums)+1)]
        
#         for num in nums:
#             t = dp[-1][:]
#             t[num] += 1
#             dp.append(t)

#         for a, b in queries:
#             diff = [i for x, y, i in zip(dp[b+1], dp[a], range(N+1)) if y != x]
#             ans.append(min([b-a for a,b in zip(diff, diff[1:])] or [-1]))
        
#         return ans


class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(nums), len(queries)
        mp = defaultdict(list)
        for i, x in enumerate(nums):
            mp[x].append(i)
        ans = [-1]*m
        # print(mp)
        for i in range(m):
            a, b = queries[i]
            arr = []
            for x in range(1,101):
                if len(mp[x]) == 0:
                    continue
                lo = bisect.bisect_left(mp[x], a)
                hi = bisect.bisect_right(mp[x], b)
                if lo < hi:
                    arr.append(x)
            # print(arr)
            if len(arr) > 1:
                ans[i] = min(b-a for a, b in zip(arr,arr[1:]))
        return ans 
