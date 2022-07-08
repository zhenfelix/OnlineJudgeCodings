class Solution:
    def confusingNumberII(self, n: int) -> int:
        sz = len(str(n))
        N = n 
        base = 1
        fac = [1]
        idx = 0
        confusing = [0,1,6,8,9]
        mp = {0:0, 1:1, 6:9, 8:8, 9:6}
        while base <= N:
            idx += 1
            base *= 10
            fac.append(fac[-1]*5)
        base //= 10
        idx -= 1

        cnt = 0
        while n:
            d = n//base
            cnt += sum(1 for c in confusing if c < d)*fac[idx]
            if d not in confusing:
                break
            n %= base
            base //= 10
            idx -= 1
        cnt += n==0

        # print(cnt)
        # print(sum(1 for i in range(N+1) if all(ch in "01689" for ch in str(i))))

        def dfs(cur):
            ans = 0
            for i in confusing:
                nxt = str(mp[i])+cur+str(i)
                
                if len(nxt) > sz:
                    return ans
                if int(nxt) > N:
                    continue
                if nxt[0] != '0':
                    ans += 1
                    # print(nxt)
                ans += dfs(nxt)
            return ans

        for i in [0,1,8]:
            if i <= N:
                cnt -= 1
                cnt -= dfs(str(i))
        cnt -= dfs('')
        return cnt