class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         res = -float('inf')
#         pos, neg = [], []
#         for a in nums:
#             if a >= 0:
#                 pos.append(a)
#             else:
#                 neg.append(a)
#         pos.sort()
#         neg.sort()
#         for i in range(4):
#             if i&1:
#                 if len(neg) >= i and len(pos) >= 3-i:
#                     cur = neg[-i:] + pos[:3-i]
#                     res = max(res, reduce(lambda x,y: x*y, cur, 1))
#             else:
#                 if len(neg) >= i and len(pos) >= 3-i:
#                     cur = neg[:i] + pos[i-3:]
#                     res = max(res, reduce(lambda x,y: x*y, cur, 1))
#         return res 


    # def maximumProduct(self, nums):
    #         nums.sort()
    #         return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

    def maximumProduct(self, nums):
            a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
            return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])