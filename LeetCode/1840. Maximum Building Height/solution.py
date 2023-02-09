class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1,0])
        restrictions.append([n,inf])
        restrictions.sort()
        m = len(restrictions)
        for i in range(m-1)[::-1]:
            dist = restrictions[i+1][0]-restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1]+dist)
        # print(restrictions)
        ans = 0
        for i in range(1,m):
            dist = restrictions[i][0]-restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1]+dist)
            mi, mx = restrictions[i][1], restrictions[i-1][1]
            if mx < mi:
                mi, mx = mx, mi 
            ans = max(ans, mi+(mx-mi+dist)//2)
            # print(mi+(mx-mi+dist+1)//2)
        # print(restrictions)
        return ans



# class Solution:
#     def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
#         res, cur = 0, 0
#         restrictions.append([1,0])
#         restrictions.sort()
        
#         st = []
#         for idx, h in restrictions:
#             while st:
#                 idx_pre, h_pre = st[-1]
#                 hi = h + (idx-idx_pre)
#                 if h_pre <= hi:
#                     break
#                 st.pop()
#             st.append([idx,h])
#         restrictions = st

#         m = len(restrictions)
#         for i in range(1,m):
#             idx, h = restrictions[i]
#             idx_pre, h_pre = restrictions[i-1]
#             lo = h - (idx-idx_pre)
#             hi = h + (idx-idx_pre)
#             if lo <= cur <= hi:
#                 res = max(res, (cur+h+(idx-idx_pre))//2)
#             cur = min(h, cur+(idx-idx_pre))
#             res = max(res,cur)
#             # print(idx,cur,res)
#         idx, h = restrictions[-1]
#         res = max(res, cur+(n-idx))
#         return res


class Solution:
    def maxBuilding(self, n: int, arr: List[List[int]]) -> int:
        arr.extend([[1, 0], [n, n - 1]])
        arr.sort()
        m = len(arr)
        
        for i in range(1, m):
            arr[i][1] = min(arr[i][1], arr[i-1][1] + arr[i][0] - arr[i-1][0])
        for i in range(m - 2, -1, -1):
            arr[i][1] = min(arr[i][1], arr[i+1][1] + arr[i+1][0] - arr[i][0])
        
        ans = 0
        for i in range(1, m):
            l, h1 = arr[i-1]
            r, h2 = arr[i]
            ans = max(ans, (r - l + h1 +h2) // 2)
        return ans