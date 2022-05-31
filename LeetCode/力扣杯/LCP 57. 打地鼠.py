class Solution:
    def getMaximumNumber(self, moles: List[List[int]]) -> int:
        mp = defaultdict(set)
        for t, x, y in moles:
            mp[t].add((x,y))
        arr = sorted(mp.keys())
        dp = [[-float('inf')]*3 for _ in range(3)]
        dp[1][1] = 0
        pre = 0
        # print(len(arr))
        # print(arr)
        # print(mp[arr[0]])
        for cur in arr:
            delta = cur-pre
            ndp = [[0]*3 for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    ndp[i][j] = dp[i][j]
                    for pi in range(3):
                        for pj in range(3):
                            if abs(i-pi)+abs(j-pj) <= delta:
                                ndp[i][j] = max(ndp[i][j], dp[pi][pj])
                    if (i,j) in mp[cur]:
                        ndp[i][j] += 1
            dp = ndp
            pre = cur
        print(dp)
        print(max(dp))
        return max(map(max,dp))