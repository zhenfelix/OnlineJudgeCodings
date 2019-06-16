# class Solution:
#     def bitwiseComplement(self, N: int) -> int:
#         if N==0: return 1
#         sums=1
#         while sums<=N:
#             sums *= 2
#         return sums-1-N
    
    
class Solution:    
    def bitwiseComplement(self, N):
        X = 1
        while N > X: X = X * 2 + 1
        return X - N