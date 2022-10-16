class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9+7
        cur = 1
        arr = []
        while n:
            if n&1:
                arr.append(cur)
            cur *= 2
            n //= 2
        ans = []
        # print(arr)
        for l, r in queries:
            cur = 1
            for i in range(l,r+1):
                cur *= arr[i]
                cur %= MOD
            ans.append(cur)
        return ans 
