# class Solution:
#     def getMaximumNumber(self, moles: List[List[int]]) -> int:
#         mp = defaultdict(set)
#         for t, x, y in moles:
#             mp[t].add((x,y))
#         arr = sorted(mp.keys())
#         dp = [[-float('inf')]*3 for _ in range(3)]
#         dp[1][1] = 0
#         pre = 0
#         # print(len(arr))
#         # print(arr)
#         # print(mp[arr[0]])
#         for cur in arr:
#             delta = cur-pre
#             ndp = [[0]*3 for _ in range(3)]
#             for i in range(3):
#                 for j in range(3):
#                     ndp[i][j] = dp[i][j]
#                     for pi in range(3):
#                         for pj in range(3):
#                             if abs(i-pi)+abs(j-pj) <= delta:
#                                 ndp[i][j] = max(ndp[i][j], dp[pi][pj])
#                     if (i,j) in mp[cur]:
#                         ndp[i][j] += 1
#             dp = ndp
#             pre = cur
#         print(dp)
#         print(max(dp))
#         return max(map(max,dp))


class Solution:
    def getMaximumNumber(self, moles: List[List[int]]) -> int:
        moles.sort()
        moles = [[0,1,1]]+moles
        n = len(moles)
        dp = [-float('inf')]*n 
        dp[0] = 0
        mx = [-float('inf')]*n 
        mx[0] = 0
        ans = 0
        for i in range(1,n):
            for j in range(i)[::-1]:
                t = moles[i][0] - moles[j][0]
                d = abs(moles[i][1]-moles[j][1]) + abs(moles[i][2]-moles[j][2])
                if t > 4:
                    dp[i] = max(dp[i], mx[j]+1)
                    break
                elif t >= d:
                    dp[i] = max(dp[i], dp[j]+1)
            ans = max(ans, dp[i])
            mx[i] = max(mx[i-1], dp[i])

        return ans