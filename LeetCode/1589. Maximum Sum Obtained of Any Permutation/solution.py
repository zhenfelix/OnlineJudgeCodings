class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        changes = [0]*(n+1)
        for a, b in requests:
            changes[a] += 1
            changes[b+1] -= 1
        cur, q = 0, []
        for i in range(n):
            cur += changes[i]
            q.append(cur)
        res, MOD = 0, 10**9+7
        for time, val in zip(sorted(q),sorted(nums)):
            res += time*val
            res %= MOD
        return res 