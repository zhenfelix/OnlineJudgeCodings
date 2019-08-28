# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         mp, memo = {}, {}
#         n = len(envelopes)
#         for i in range(n):
#             mp[i] = []
        
#         for i in range(n):
#             for j in range(i+1,n,1):
#                 if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
#                     mp[i] += [j]
#                 elif envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
#                     mp[j] += [i]
                    
#         def dfs(idx):
#             if idx in memo:
#                 return memo[idx]
#             dis = 0
#             for k in mp[idx]:
#                 dis = max(dis, dfs(k))
#             dis += 1
#             memo[idx] = dis
#             return dis
        
#         ans = 0
#         for i in range(n):
#             ans = max(ans, dfs(i))
#         return ans


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        def lower_bound(arr, target):
            left, right = 0, len(arr)-1
            while left <= right:
                mid = (left+right)//2
                if target > arr[mid]:
                    left = mid+1
                else:
                    right = mid-1
            return left
        st = []
        for e in envelopes:
            idx = lower_bound(st, e[1])
            if idx == len(st):
                st.append(e[1])
            else:
                st[idx] = e[1]
        # print(envelopes)
        # print(st)
        return len(st)
        