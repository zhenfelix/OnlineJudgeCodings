# class Solution:
#     def minMoves(self, nums: List[int], limit: int) -> int:
#         change = [0]*(2*limit+5)
#         cc = Counter()
#         n = len(nums)
#         for i in range(n//2):
#             a, b = nums[i], nums[n-1-i]
#             cc[a+b] += 1
#             change[min(a,b)+1] += 1
#             change[max(a,b)+1+limit] -= 1
#         res, cnt = n, 0
#         for cur in range(2,limit*2+1):
#             cnt += change[cur]
#             res = min(res, cnt-cc[cur]+n-2*cnt)
#         return res 

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        delta = [0]*(2*limit+2)
        n = len(nums)
        for i in range(n//2):
            a, b = nums[i], nums[n-i-1]
            mi, mx = min(a,b), max(a,b)
            delta[mi+1] -= 1
            delta[mi+mx] -= 1
            delta[mi+mx+1] += 1
            delta[mx+limit+1] += 1
        ans = cur = n 
        for v in range(2,limit*2+1):
            cur += delta[v]
            ans = min(ans, cur)
        return ans

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        delta = collections.Counter()
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            delta[2] += 2
            delta[min(a, b) + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[max(a, b) + limit + 1] += 1
            
        curr = 0            
        res = math.inf
        for i in range(2, 2 * limit + 1):
            curr += delta[i]
            res = min(res, curr)
        return res   