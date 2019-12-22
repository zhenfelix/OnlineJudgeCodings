# class Solution:
#     def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
#         res = []
#         left, right = toBeRemoved[0], toBeRemoved[1]
#         for a, b in intervals:
#             if b <= left or a >= right:
#                 res.append([a,b])
#             elif a < left and right < b:
#                 res.append([a,left])
#                 res.append([right,b])
#             elif a < left:
#                 res.append([a,min(b,left)])
#             elif right < b:
#                 res.append([max(a,right),b])
#         return res
            

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        for lo, hi in intervals:
            remove_lo, remove_hi = toBeRemoved
            if hi <= remove_lo or lo >= remove_hi:
                ans.append([lo, hi])
            else:
                if lo < remove_lo:
                    ans.append([lo, remove_lo])
                if hi > remove_hi:
                    ans.append([remove_hi, hi])
        return ans

