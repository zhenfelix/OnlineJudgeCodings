class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD, res = 10**9+7, 0
        cnt = Counter()
        for x in deliciousness:
            base = 1
            for i in range(22):
                res += cnt[base-x]
                base *= 2
            res %= MOD
            cnt[x] += 1
        return res 