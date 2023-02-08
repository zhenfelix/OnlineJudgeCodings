class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = mx = 0
        for a in nums:
            cur = 0
            while a:
                ans += (a&1)
                a >>= 1
                cur += (a>0)
            mx = max(mx, cur)
        return ans+mx

class Solution:
    def minOperations(self, A):
        return sum(bin(a).count('1') for a in A) + len(bin(max(A))) - 3        

# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         mul, add = 0, 0
#         for cur in nums:
#             cur = bin(cur)[2:]
#             mul = max(mul, len(cur)-1)
#             add += cur.count('1')
#         return mul+add