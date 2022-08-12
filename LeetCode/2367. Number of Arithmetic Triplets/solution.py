class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        ans = 0
        seen = set(nums)
        for x in nums:
            if x+diff in seen and x-diff in seen:
                ans += 1
        return ans

# class Solution:
#     def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
#         n = len(nums)
#         ans = 0
#         left, right = set(), set(nums)
#         for x in nums:
#             right.remove(x)
#             if x+diff in right and x-diff in left:
#                 ans += 1
#             left.add(x)
#         return ans