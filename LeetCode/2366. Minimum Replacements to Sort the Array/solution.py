class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        cnt = 0
        pre = nums[-1]
        for cur in nums[::-1]:
            delta = (cur-1)//pre+1
            cnt += delta - 1
            pre = cur//delta

        return cnt 

# class Solution:
#     def minimumReplacement(self, nums: List[int]) -> int:
#         def calc(x, limit):
#             lo, hi = 1, x
#             while lo <= hi:
#                 mid = (lo+hi)//2
#                 # if x == 15:
#                 #     print(lo,hi,x%mid,x//mid)
#                 if (x-1)//mid+1 <= limit:
#                     hi = mid - 1
#                 else:
#                     lo = mid + 1
#             return lo 

#         cnt = 0
#         pre = float('inf')
#         for cur in nums[::-1]:
#             if cur > pre:
#                 delta = calc(cur,pre)
#                 cnt += delta - 1
#                 pre = cur//delta
#                 # print(cur,delta,pre)
#             else:
#                 pre = cur

#         return cnt 


