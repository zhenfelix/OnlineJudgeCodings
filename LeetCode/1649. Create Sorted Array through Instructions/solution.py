class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n = max(instructions)
        arr = [0]*(n+1)
        def query(x):
            cnt = 0
            while x > 0:
                cnt += arr[x]
                x -= (x&(-x))
            return cnt
        def update(x):
            while x <= n:
                arr[x] += 1
                x += (x&(-x))
            return
        res, MOD = 0, 10**9+7
        for i, cur in enumerate(instructions):
            res += min(query(cur-1),i-query(cur))
            res %= MOD
            update(cur)
        return res 