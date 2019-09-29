class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = sums = 0
        n = len(s)
        arr = [abs(ord(s[i])-ord(t[i])) for i in range(n)]
        left, right = 0, 0
        while right < n:
            sums += arr[right]
            while sums > maxCost:
                sums -= arr[left]
                left += 1
            ans = max(ans, right-left+1)
            right += 1
        
        return ans

    
#     def equalSubstring(self, s, t, cost):
#         A = [abs(ord(i) - ord(j)) for i, j in zip(s, t)]
#         i = 0
#         for j in range(len(s)):
#             cost -= A[j]
#             if cost < 0:
#                 cost += A[i]
#                 i += 1
#         return j - i + 1
            



# class Solution:
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         def great_eq(val):
#             left, right = 0, len(sums)-1
#             while left <= right:
#                 mid = (left+right)//2
#                 if sums[mid] >= val:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             return left
            
            
#         n = len(s)
#         arr = [abs(ord(s[i])-ord(t[i])) for i in range(n)]
#         # print(arr)
#         ans = 0
#         sums = [0]
#         for i in range(n):
#             sums.append(sums[-1]+arr[i])
#             idx = great_eq(sums[-1]-maxCost)
#             # print(i,idx,len(sums)-idx-1)
#             ans = max(ans, len(sums)-idx-1)
            
#         # print(sums)
#         return ans