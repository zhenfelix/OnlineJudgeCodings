# class Solution:
#     def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
#         staple.sort()
#         drinks.sort()
#         n, m = len(staple), len(drinks)
#         cnt, j = 0, m-1
#         MOD = 10**9 + 7
#         for i in range(n):
#             while j >= 0 and staple[i] + drinks[j] > x:
#                 j -= 1
#             cnt += j+1
#             cnt %= MOD
#         return cnt 


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        ans = 0
        arr = [0 for i in range(x+1)]
        
        for sta in staple:
            if sta < x:
                arr[sta] += 1
        
        for i in range(2, x):
            arr[i] += arr[i-1]
        
        for drink in drinks:
            lt = x - drink
            if lt <= 0:
                continue
            ans += arr[lt]
            
        return ans % (10 ** 9 + 7)
        
