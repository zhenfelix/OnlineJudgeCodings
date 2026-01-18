class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        cnt = delta = ans = 0
        for a,b in zip(s,t):
            if a != b:
                cnt += 1
                if a == '1':
                    delta += 1
                else:
                    delta -= 1
        delta = abs(delta)
        if cnt&1:
            ans += flipCost
            cnt -= 1
            delta -= 1
        # print(cnt,delta)
        ans += min(flipCost*delta+min((cnt-delta)*flipCost,(cnt-delta)//2*swapCost),crossCost*delta//2+min(cnt*flipCost,cnt//2*swapCost))
        return ans 

