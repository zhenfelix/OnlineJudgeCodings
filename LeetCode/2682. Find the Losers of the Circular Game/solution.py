class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cnt = [0]*n 
        cur = 0
        for i in range(n+1):
            cnt[cur] += 1
            if cnt[cur] >= 2: break
            # print(cnt,cur)
            cur += (i+1)*k
            cur %= n  
            
        ans = [i+1 for i in range(n) if cnt[i] == 0]
        return ans 