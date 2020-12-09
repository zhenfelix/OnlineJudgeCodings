class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [0]*n, [0]*n 
        st = []
        for i in range(n):
            idx = bisect.bisect_left(st,nums[i])
            if idx == len(st):
                st.append(-1)
            st[idx] = nums[i]
            left[i] += idx+1
        st = []
        for i in range(n)[::-1]:
            idx = bisect.bisect_left(st,nums[i])
            if idx == len(st):
                st.append(-1)
            st[idx] = nums[i]
            right[i] += idx+1
        # print(left,right)
        return n-max(left[i]+right[i]-1 for i in range(n) if left[i]>1 and right[i]>1)


class Solution:
    def minimumMountainRemovals(self, nums):
        def LIS(nums):
            dp = [10**10] * (len(nums) + 1)
            lens = [0]*len(nums)
            for i, elem in enumerate(nums): 
                lens[i] = bisect_left(dp, elem) + 1
                dp[lens[i] - 1] = elem 
            return lens
        
        l1, l2 = LIS(nums), LIS(nums[::-1])[::-1]
        ans, n = 0, len(nums)
        for i in range(n):
            if l1[i] >= 2 and l2[i] >= 2:
                ans = max(ans, l1[i] + l2[i] - 1)
                
        return n - ans

# class Solution:
#     def minimumMountainRemovals(self, nums: List[int]) -> int:
#         n = len(nums)
#         left, right = [0]*n, [0]*n
#         for i in range(n):
#             left[i] = 1
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     left[i] = max(left[i], left[j]+1)
#         for i in range(n)[::-1]:
#             right[i] = 1
#             for j in range(i+1,n):
#                 if nums[j] < nums[i]:
#                     right[i] = max(right[i], right[j]+1)
#         # print(left,right)
#         return n-max(left[i]+right[i]-1 for i in range(n) if left[i]>1 and right[i]>1)