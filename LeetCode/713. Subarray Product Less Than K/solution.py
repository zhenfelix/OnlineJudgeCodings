# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         cur, j, res = 1, -1, 0
#         ss = set()
#         for i in range(len(nums)):
#             j = max(i-1,j)
#             while j+1 < len(nums) and cur*nums[j+1] < k:
#                 cur *= nums[j+1]
#                 j += 1
#             res += j - i + 1
#             ss.add(j)
#             # print(i,j,cur)
#             cur //= nums[i]
#         print(ss)
#         return res 


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cur, i, res = 1, 0, 0
        # print(Counter(nums))
        for j in range(len(nums)):
            cur *= nums[j]
            while i <= j and cur >= k:
                cur //= nums[i]
                i += 1
            res += j - i + 1
        return res 