class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        cnt, n = 0, len(row)//2
        mp = [-1]*n*2
        for i, r in enumerate(row):
            mp[r] = i 
        for j in range(n):
            i = j
            while row[i*2]//2 != row[i*2+1]//2:
                nxt = mp[row[i*2]//2*4+1-row[i*2]]
                row[i*2+1], row[nxt] = row[nxt], row[i*2+1]
                mp[row[i*2+1]], mp[row[nxt]] = nxt, i*2+1
                i = nxt//2
                cnt += 1
        return cnt