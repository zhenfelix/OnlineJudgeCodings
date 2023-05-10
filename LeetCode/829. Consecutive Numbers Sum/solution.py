# class Solution(object):
#     def consecutiveNumbersSum(self, N):
#         """
#         :type N: int
#         :rtype: int
#         """
#         res = 1
#         left, right = N//2, N//2 + 1
#         while right > 0:
#             while left > 0 and (left+right)*(right-left+1)//2 < N:
#                 left -= 1
#             if left == 0:
#                 break
#             if (left+right)*(right-left+1)//2 == N:
#                 # print(left,right)
#                 res += 1
#             right -= 1
#         return res

#      

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        n *= 2 
        f = 1
        ans = 0
        while f*f <= n:
            if n%f == 0:
                af = n//f 
                af += 1-f
                if af > 0 and af%2 == 0:
                    ans += 1
                # af = n//f 
                # f += 1-af 
                # if f > 0 and f%2 == 0:
                #     ans += 1
                # f = n//af 
            f += 1
        return ans 

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        def isKConsecutive(n: int, k: int) -> bool:
            if k % 2:
                return n % k == 0
            return n % k and 2 * n % k == 0

        ans = 0
        k = 1
        while k * (k + 1) <= n * 2:
            if isKConsecutive(n, k):
                ans += 1
            k += 1
        return ans


# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/consecutive-numbers-sum/solution/lian-xu-zheng-shu-qiu-he-by-leetcode-sol-33hc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。   
import math
class Solution(object):
    # def consecutiveNumbersSum(self, N):
    #     """
    #     :type N: int
    #     :rtype: int
    #     """
    #     res = 0
    #     for m in range(1,int(math.sqrt(2*N))+1):
    #         if (2*N)%m == 0 and ((2*N//m)+1-m)%2 == 0:
    #             res += 1
    #     return res
    
    def consecutiveNumbersSum(self, N):
        res = 1
        i = 3
        while N % 2 == 0:
            N //= 2
        while i * i <= N:
            count = 0
            while N % i == 0:
                N //= i
                count += 1
            res *= count + 1
            i += 2
        return res if N == 1 else res * 2

        