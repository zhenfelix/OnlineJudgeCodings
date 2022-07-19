# import heapq

# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)
#         arr = []
#         for i, _ in enumerate(ratings):
#             arr.append(i)
#         arr = sorted(arr, key=lambda x: ratings[x])
#         ans = [1]*n
        
#         for idx in arr:
#             cur = idx
#             if ans[cur] == 1:
#                 while cur+1 < n and ratings[cur+1] > ratings[cur]:
#                     ans[cur+1] = max(ans[cur+1], ans[cur]+1)
#                     cur += 1
#                 cur = idx
#                 while cur-1 >= 0 and ratings[cur-1] > ratings[cur]:
#                     ans[cur-1] = max(ans[cur-1], ans[cur]+1)
#                     cur -= 1
#         print(ans)                  
#         return sum(ans)


# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)

#         ans = [1]*n
        
#         for idx in range(n):
#             cur = idx
#             if cur > 0 and cur < n-1 and ((ratings[cur] > ratings[cur-1] and ratings[cur] < ratings[cur+1]) or (ratings[cur] < ratings[cur-1] and ratings[cur] > ratings[cur+1])):
#                 continue

#             while cur+1 < n and ratings[cur+1] > ratings[cur]:
#                 ans[cur+1] = max(ans[cur+1], ans[cur]+1)
#                 cur += 1
#             cur = idx
#             while cur-1 >= 0 and ratings[cur-1] > ratings[cur]:
#                 ans[cur-1] = max(ans[cur-1], ans[cur]+1)
#                 cur -= 1
        
#         # print(ans)                  
#         return sum(ans)

# class Solution:
#     def candy(self, ratings: List[int]) -> int:
        
#         if not ratings:
#             return 0
        
#         if len(ratings) <= 1:
#             return len(ratings)
        
#         dp = [1] * len(ratings)
        
#         for i in range(1, len(ratings)):
#             if ratings[i] > ratings[i-1]:
#                 dp[i] = dp[i-1] + 1
        
#         for i in reversed(range(len(ratings)-1)):
#             if ratings[i] > ratings[i+1]:
#                 dp[i] = max(dp[i+1] + 1, dp[i])
        
#         return sum(dp)

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n <= 1:
            return n
            
        # initial state: each kid gets one candy    
        nums = [1] * n
        # kids on upwards curve get candies
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1] + 1

        # kids on downwards curve get candies
        # if a kid on both up/down curves, i.e. a peak or a valley
        # kid gets the maximum candies among the two.
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                nums[i-1] = max(nums[i]+1, nums[i-1])
   
        return sum(nums)
        

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        cnt = [1]*n 
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                cnt[i] = max(cnt[i], cnt[i-1]+1)
        for i in range(n-1)[::-1]:
            if ratings[i] > ratings[i+1]:
                cnt[i] = max(cnt[i], cnt[i+1]+1)
        return sum(cnt)