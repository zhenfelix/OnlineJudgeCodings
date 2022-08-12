# class Solution:
#     def sumOddLengthSubarrays(self, arr: List[int]) -> int:
#         sums, res = [0], 0
#         for a in arr:
#             a += sums[-1]
#             for pre in sums[-1::-2]:
#                 res += a - pre
#             sums.append(a)
#         return res


class Solution:
    # def sumOddLengthSubarrays(self, arr: List[int]) -> int:
    #     res, n = 0, len(arr)
    #     odd, even = 0, 0
    #     for i in range(n):
    #         delta_odd = (i//2 + 1)*arr[i]
    #         delta_even = ((i+1)//2)*arr[i]
    #         odd, even = even+delta_odd, odd+delta_even
    #         res += odd
    #         # print(odd, even, res)
    #     return res
    
    def sumOddLengthSubarrays(self, A):
        res, n = 0, len(A)
        for i, a in enumerate(A):
            res += ((i + 1) * (n - i) + 1) // 2 * a
        return res

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i, x in enumerate(arr):
            left, right = i+1, n-i-1
            # print(i,left,right,left//2*((right+1)//2),(left+1)//2*((right+2)//2))
            ans += (left//2*((right+1)//2)+(left+1)//2*((right+2)//2))*x
        return ans