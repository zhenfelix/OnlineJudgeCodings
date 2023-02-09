class Solution:
    def countPalindromes(self, s: str) -> int:
        n = len(s)
        MOD = 10**9+7  
        ans = 0
        def calc(arr):
            sums = [Counter() for _ in range(10)]
            cc = Counter()
            dp = []
            for a in arr:
                a = int(a)
                
                for j in range(10):
                    sums[a][j] += cc[j]
                dp.append([sums[i].copy() for i in range(10)])
                # print(a,sums, cc)
                cc[a] += 1
            return dp 

        left, right = calc(s), calc(s[::-1])[::-1]
        # print(left[:3])
        for i in range(1,n-1):
            for a in range(10):
                for b in range(10):
                    # if left[i-1][a][b] or right[i+1][a][b]:
                    #     print(i,a,b,left[i-1][a][b],right[i+1][a][b])
                    ans = (ans+left[i-1][a][b]*right[i+1][a][b])%MOD 


        return ans

