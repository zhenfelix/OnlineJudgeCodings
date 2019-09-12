# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         n, m = len(s), len(t)
#         i, j = 0 ,0
#         while i < n and j < m:
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
#         return i == n
                
# class Solution:
#     def isSubsequence(self, s, t):
#         t = iter(t)
#         return all(c in t for c in s)

import collections

class Solution:
    def isSubsequence(self, s, t):
        def lower_bound(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return left
        
        mp = collections.defaultdict(list)
        for i, ch in enumerate(t):
            mp[ch].append(i)
        
        pre = -1
        for ch in s:
            j = lower_bound(mp[ch], pre)
            if j == len(mp[ch]):
                return False
            pre = mp[ch][j]
        return True