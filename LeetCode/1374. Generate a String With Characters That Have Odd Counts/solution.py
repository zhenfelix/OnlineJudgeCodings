class Solution:
#     def generateTheString(self, n: int) -> str:
#         if n & 1:
#             return "a"*n
#         return "a"+"b"*(n-1)
            
    def generateTheString(self, n):
        return 'b' + 'ab'[n & 1] * (n - 1)