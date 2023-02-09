class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        cc = Counter()
        for p in nums:
            cc[p%space] += 1
        ans, cnt = nums[0], cc[nums[0]%space]
        
        for p in nums:
            cur = cc[p%space]
            if cur > cnt or (cur == cnt and p < ans):
                ans = p 
                cnt = cur 
        return ans


# class Solution:
#     def destroyTargets(self, nums: List[int], space: int) -> int:
#         cc = Counter()
#         for p in nums:
#             cc[p%space] += 1
#         ans, cnt = [], 0
#         for k, v in cc.items():
#             if v > cnt:
#                 ans = [k]
#                 cnt = v 
#             elif v == cnt:
#                 ans.append(k)
#         ans = set(ans)
#         nums.sort()
#         for p in nums:
#             if (p%space) in ans:
#                 return p 
#         return -1
