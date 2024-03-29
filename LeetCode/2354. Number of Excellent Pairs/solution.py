class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        def convert(x):
            cnt = 0
            while x:
                cnt += (x&1)
                x >>= 1
            return cnt
        nums = sorted(list(map(convert,set(nums))))
        n = len(nums)
        ans = 0
        j = n-1
        for i in range(n):
            while j >= 0 and nums[i]+nums[j] >= k:
                j -= 1
            ans += n-j-1
        return ans 
        


class Solution:
    def countExcellentPairs(self, nums: List[int], m: int) -> int:
        nums = list(set(nums))
        n = len(nums)
        cc = [0]*n 
        sums = [0]*32
        ans = 0
        for i, cur in enumerate(nums):
            for j in range(32):
                if (cur>>j)&1 == 1:
                    cc[i] += 1
            sums[cc[i]] += 1
        
        for i in range(32):
            for j in range(32):
                if i + j >= m:
                    ans += sums[i]*sums[j]
        return ans

# class Solution:
#     def countExcellentPairs(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         cc = Counter(nums)
#         bcnt = Counter()
#         mp = defaultdict(int)
#         tot = 0
#         ans = 0
#         for k, v in cc.items():
#             for i in range(32):
#                 if (k>>i)&1 == 1:
#                     bcnt[k] += 1
#             mp[bcnt[k]] += 1
#             tot += 1
        
#         for k, v in cc.items():
#             if bcnt[k] >= m:
#                 ans += tot
#             else:
#                 for i in range(32):
#                     if i+bcnt[k] >= m:
#                         ans += mp[i]
#         return ans 