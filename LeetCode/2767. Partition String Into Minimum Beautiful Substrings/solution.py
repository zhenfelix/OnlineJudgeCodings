class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        if s[0] == '0': return -1
        n = len(s)
        seen = set()
        cur = 1
        while cur < (1<<20):
            seen.add(cur)
            cur *= 5
        # print(seen)
        @lru_cache(None)
        def dfs(i,v):
            if i == n:
                return inf if v not in seen else 1
            ans = inf  
            d = int(s[i])
            if d != 0 and v in seen:
                ans = min(ans,1+dfs(i+1,1))
            ans = min(ans,dfs(i+1,v*2+d))
            return ans 
        res = dfs(0,0)
        return res if res < inf else -1


# 预处理 2**15 以内的 5 的幂
pow5 = [bin(5 ** i)[2:] for i in range(7)]

class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i: int) -> int:
            if i == n: return 0
            if s[i] == '0': return inf  # 不能包含前导 0
            res = inf
            for t in pow5:
                if i + len(t) > n:
                    break
                if s[i: i + len(t)] == t:  # 忽略切片的时间，这里的比较视作均摊 O(1)
                    res = min(res, dfs(i + len(t)) + 1)
            return res
        ans = dfs(0)
        return ans if ans < inf else -1


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/partition-string-into-minimum-beautiful-substrings/solution/on2-ji-yi-hua-sou-suo-dao-di-tui-by-endl-99lb/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。