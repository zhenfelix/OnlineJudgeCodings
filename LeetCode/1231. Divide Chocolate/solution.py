# class Solution:
#     def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
#         def dfs(left,right,k):
#             # print(left,right,k)
#             if (left,right,k) in memo:
#                 return memo[left,right,k]
#             if k == 0:
#                 memo[left,right,k] = sum(sweetness[left:right+1])
#                 return memo[left,right,k]
#             if right-left == k:
#                 memo[left,right,k] = min(sweetness[left:right+1])
#                 return memo[left,right,k]
#             res = 0
#             # sums = 0
#             # print(left,right,k)
#             lo, hi = left+k+1, right-left
#             while lo <= hi:
#                 mid = (lo+hi)//2
#                 if dfs(left,mid-1,k-1) > sum(sweetness[mid:right+1]):
#                     hi = mid-1
#                 else:
#                     lo = mid+1
#             res_right = max(dfs(left,hi-1,k-1),sum(sweetness[lo:right+1]))
#             # for i in range(right,left+k,-1):
#             #     sums += sweetness[i]
#             #     res = max(res,min(dfs(left,i-1,k-1),sums))
#                 # print(left,right,k,i,res)
#             lo, hi = left, right-k-1
#             while lo <= hi:
#                 mid = (lo+hi)//2
#                 if dfs(mid+1,right,k-1) > sum(sweetness[left:mid]):
#                     lo = mid+1
#                 else:
#                     hi = mid-1
#             res_left = max(dfs(lo+1,right,k-1),sum(sweetness[left:hi]))


#             # sums = 0
#             # for i in range(left,right-k,1):
#             #     sums += sweetness[i]
#             #     res = max(res,min(dfs(i+1,right,k-1),sums))

#             memo[left,right,k] = max(res_left,res_right)
#             return memo[left,right,k]
#         memo = {}
#         dfs(0,len(sweetness)-1,K)
#         # print(memo)
#         return memo[0,len(sweetness)-1,K]


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        lo, hi = 1, sum(sweetness)//(K+1)
        while lo <= hi:
            mid = (lo+hi)//2
            cur = cuts = 0
            for x in sweetness:
                cur += x
                if cur >= mid:
                    cur, cuts = 0, cuts+1
                if cuts > K:
                    break
            if cuts > K:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi