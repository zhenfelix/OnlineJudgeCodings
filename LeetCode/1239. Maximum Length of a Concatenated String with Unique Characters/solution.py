class Solution:
    # def maxLength(self, arr: List[str]) -> int:
    #     arr = [set(a) for a in arr if len(a) == len(set(a))]
    #     print(arr)
    #     if not arr:
    #         return 0
    #     n = len(arr)
    #     res = [0]
    #     def dfs(idx, path):
    #         if idx == n:
    #             res[0] = max(res[0], len(path))
    #             return
    #         dfs(idx+1, path)
    #         if len(path.union(arr[idx])) == len(path) + len(set(arr[idx])):
    #             dfs(idx+1, path.union(arr[idx]))
    #         return
    #     # dp = [set(a) for a in arr]
    #     # for i in range(n):
    #     #     for j in range(i):
    #     #         if len(dp[j].union(set(arr[i]))) == len(dp[j])+len(set(arr[i])) and len(dp[j].union(set(arr[i]))) > len(dp[i]):
    #     #             dp[i] = dp[j].union(set(arr[i]))
    #     # print(dp)
    #     dfs(0,set())
    #     return res[0]
    
    def maxLength(self, A):
        dp = [set()]
        for a in A:
            if len(set(a)) != len(a): continue
            a = set(a)
            for c in dp[:]:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)