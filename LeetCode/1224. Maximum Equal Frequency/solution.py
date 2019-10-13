# from collections import Counter

# class Solution:
#     def maxEqualFreq(self, nums: List[int]) -> int:
#         cc = Counter(nums)
#         cnt = Counter()
#         n = len(nums)
#         for k, v in cc.items():
#             cnt[v] += v
        
        
#         while n > 0:
#             # print(cc)
#             # print(cnt)
#             # print(nums[n-1])
#             if len(cnt) == 2:
#                 a, b = list(cnt.keys())
#                 # print(a,b)
#                 if cnt[1] == 1 or (abs(a-b) == 1 and max(a,b) == cnt[max(a,b)]):
#                     return n
#             elif len(cnt) == 1:
#                 a = list(cnt.keys())[0]
#                 if cnt[1] > 1 or cnt[a] == a:
#                     return n
#             cnt[cc[nums[n-1]]] -= cc[nums[n-1]]
#             if cnt[cc[nums[n-1]]] == 0:
#                 del cnt[cc[nums[n-1]]]
#             cc[nums[n-1]] -= 1
#             if cc[nums[n-1]] > 0:
#                 cnt[cc[nums[n-1]]] += cc[nums[n-1]]
            
#             n -= 1

from collections import Counter

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        cnt, freq = Counter(), Counter()
        res, max_freq = 0, 0
        for i, cur in enumerate(nums):
            freq[cnt[cur]] -= cnt[cur]
            cnt[cur] += 1
            max_freq = max(max_freq, cnt[cur])
            freq[cnt[cur]] += cnt[cur]
            if freq[1] == i+1 or freq[max_freq] == i or (freq[max_freq] == max_freq and freq[max_freq-1] == i+1-max_freq):
                res = i+1
        return res
