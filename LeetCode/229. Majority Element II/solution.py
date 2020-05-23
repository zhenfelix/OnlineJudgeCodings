# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         ca, cb = 0, 0
#         for x in nums:
#             if ca == 0:
#                 a = x
#                 ca += 1
#             elif x == a:
#                 ca += 1
#             elif cb == 0:
#                 b = x
#                 cb += 1
#             elif x == b:
#                 cb += 1
#                 if cb > ca:
#                     cb, ca = ca, cb
#                     b , a = a, b
#             else:
#                 ca -= 1
#                 cb -= 1
#         # print(a, b)
#         ca, cb, n = 0, 0, len(nums)
#         for x in nums:
#             if x == a:
#                 ca += 1
#             elif x == b:
#                 cb += 1
#         ans = []
#         if ca > n//3:
#             ans.append(a)
#         if cb > n//3:
#             ans.append(b)
#         return ans


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ca, cb = 0, 0
        a, b = None, None
        for x in nums:
            if ca == 0 or a == x:
                a = x
                ca += 1
            elif cb == 0 or b == x:
                b = x
                cb += 1
            else:
                ca -= 1
                cb -= 1
            if cb > ca:
                cb, ca = ca, cb
                b, a = a, b
            # print(a, b)
        # print(a, b)
        n, ans = len(nums), []
        if ca and sum(x == a for x in nums) > n//3:
            ans.append(a)
        if cb and sum(x == b for x in nums) > n//3:
            ans.append(b)
        return ans


    def majorityElement(self, nums):
        ctr = collections.Counter()
        for n in nums:
            ctr[n] += 1
            if len(ctr) == 3:
                ctr -= collections.Counter(set(ctr))
        return [n for n in ctr if nums.count(n) > len(nums)/3]
    
# My understanding of Boyer-Moore Majority Vote
# https://leetcode.com/problems/majority-element-ii/discuss/63537/My-understanding-of-Boyer-Moore-Majority-Vote
# When I was learning about Boyer-Moore, I was always thinking about the pair. I drew a picture to get myself understandable.

