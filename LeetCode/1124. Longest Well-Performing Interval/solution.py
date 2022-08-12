class Solution:
    def longestWPI(self, hours):
        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score not in seen:
                seen[score] = i
            if score > 0:
                res = i + 1
            elif score - 1 in seen:
                res = max(res, i - seen[score - 1])
            
        return res

# class Solution:
#     def longestWPI(self, hours: List[int]) -> int:
#         hours = [1 if h > 8 else -1 for h in hours]
#         st = [(-1,0)]
#         cur = 0
#         ans = 0
#         for i, x in enumerate(hours):
#             cur += x
#             # print(st,cur)
#             lo, hi = 0, len(st)-1
#             while lo <= hi:
#                 m = (lo+hi)//2
#                 j, v = st[m]
#                 if v < cur:
#                     hi = m - 1
#                 else:
#                     lo = m + 1
#             if lo < len(st):
#                 ans = max(ans, i-st[lo][0])
#             if cur < st[-1][-1]:
#                 st.append((i,cur))
            
#         return ans 


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        hours = [1 if h > 8 else -1 for h in hours]
        n = len(hours)
        st = [(-1,0)]
        cur = 0
        ans = 0
        presums = []
        for i, x in enumerate(hours):
            cur += x
            if cur < st[-1][-1]:
                st.append((i,cur))
            presums.append(cur)
        presums.append(0)
        for i in range(n)[::-1]:
            while st and (st[-1][0] >= i or st[-1][-1] < presums[i]):
                j, _ = st.pop()
                ans = max(ans, i-j)
        return ans 