class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10**9+7
        @lru_cache(None)
        def dfs(n,k):
            if k == 0:
                return 1
            if n == 0:
                return 1
            if n < 0:
                return 0
            return sum(dfs(n-i,k) for i in range(1,k+1))%MOD
        ans, cnt = 1, 0
        pre = '0'
        mp = [3]*10
        mp[0] = mp[1] = 0
        mp[7] = mp[9] = 4
        # print(mp)
        for cur in pressedKeys+'0':
            if cur != pre:
                # print(dfs(cnt,mp[ord(pre)-ord('0')]),cnt,mp[ord(pre)-ord('0')])
                ans *= dfs(cnt,mp[ord(pre)-ord('0')])
                ans %= MOD
                cnt = 0
            cnt += 1
            pre = cur
        return ans 