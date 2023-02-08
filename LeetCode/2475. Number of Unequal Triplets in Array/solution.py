class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cc = Counter(nums)
        arr = sorted(cc)
        n = len(nums)
        cnt = ans = 0
        for k in arr:
            v = cc[k]
            ans += cnt*v*(n-v-cnt)
            cnt += v 
        return ans

# class Solution:
#     def unequalTriplets(self, nums: List[int]) -> int:
#         cc = Counter()
#         n = len(nums)
#         ans = 0
#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[j] == nums[i]:
#                     continue
#                 ans += i-cc[nums[i]]-cc[nums[j]]
#                 # print(i,j,i-cc[nums[i]]-cc[nums[j]])
#             cc[nums[i]] += 1
#         return ans