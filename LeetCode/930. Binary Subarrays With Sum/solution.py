# class Solution:
#     def numSubarraysWithSum(self, A: List[int], S: int) -> int:
#         if S>len(A):return 0
#         mp = [0]*(S+1)
#         ans = 0
#         for i, a in enumerate(A):
#             if a == 1:
#                 pre = min(i,S-1)
#                 for t in range(pre,-1,-1):
#                     mp[t+1]=mp[t]
#                 if S>0: mp[1] += 1
#                 mp[0] = 0
#             else:
#                 mp[0] += 1
#             ans += mp[S]
#         return ans

# class Solution:
#     def numSubarraysWithSum(self, A, S):
#         c = collections.Counter({0: 1})
#         psum = res = 0
#         for i in A:
#             psum += i
#             res += c[psum - S]
#             c[psum] += 1
#         return res

class Solution:
    def numSubarraysWithSum(self, bins: List[int], target: int) -> int:
        cnts = [0] * (len(bins) + 1)
        cnts[0] = 1
        
        ans = total = 0
        
        for b in bins:
            total += b
            ans += cnts[total - target]
            cnts[total] += 1
        
        return ans