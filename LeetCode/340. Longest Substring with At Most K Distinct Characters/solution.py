# class Solution:
#     def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
#         if k <= 0:
#             return 0
#         mp = {}
#         res, cur = 0, 0
#         n = len(s)
#         for i, ch in enumerate(s):
#             if ch not in mp and len(mp) == k:
#                 idx, pos = i, -1
#                 for key in mp:
#                     if mp[key] < idx:
#                         idx, pos = mp[key], key
#                 del mp[pos]
#                 cur = i - idx
#             else:
#                 cur += 1
#             mp[ch] = i
#             res = max(res, cur)
#         return res
                
# class Solution:
#     def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
#         if k <= 0 or len(s) == 0:
#             return 0
#         mp = {}
#         res = 0
#         n = len(s)
#         left, right = 0, 0
#         while right < n:
#             mp[s[right]] = right
#             if len(mp) > k:
#                 while mp[s[left]] != left:
#                     left += 1
#                 del mp[s[left]]
#                 left += 1
#             right += 1
#             res = max(res, right-left)
#         return res


from collections import Counter
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        left = right = 0
        cnt = 0
        n = len(s)
        cc = Counter()
        while left < n and right < n:
            while right < n:
                ch = s[right]
                if cc[ch] == 0:
                    cnt += 1
                if cnt > k:
                    cnt -= 1
                    break
                cc[ch] += 1
                right += 1
            # print(left,right,cnt)
            res = max(res,right-left)
            ch = s[left]
            cc[ch] -= 1
            if cc[ch] == 0:
                cnt -= 1
            left += 1
        return res
                