# class Solution:
#     def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
#         candidate = [(a,s) for a,s in zip(ages,scores)]
#         candidate.sort()
#         res, n = 0, len(candidate)
#         candidate += [(0,0)]
#         # print(candidate)
#         dp = [0]*(n+1)
#         for i in range(n):
#             a, s = candidate[i]
#             j = i-1
#             while j >= -1:
#                 ax, sx = candidate[j]
#                 if s >= sx:
#                     dp[i] = max(dp[i],dp[j]+s)
#                 j -= 1
                
#             res = max(res,dp[i])
#         return res


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        candidate = [(s,a) for a,s in zip(ages,scores)]
        candidate.sort()
        res, n = 0, len(candidate)
        # print(candidate)
        dp = [0]*(1000+1)
        for i in range(n):
            s, a = candidate[i]
            dp[a] = max(dp[j] for j in range(a+1)) + s
            # print(dp)
        # print(dp1,dp2)
        return max(dp)


class SegTree:
    def __init__(self, N):
        self.arr = [0]*(N*4)
        self.N = N

    def update(self, pos, val):
        self.update_(0, 1, self.N, pos, val)
        return

    def update_(self, idx, lo, hi, pos, val):
        if lo > pos or hi < pos:
            return
        if lo == hi:
            self.arr[idx] = val
            return
        mid = (lo + hi)//2
        self.update_(idx*2+1, lo, mid, pos, val)
        self.update_(idx*2+2, mid+1, hi, pos, val)
        self.arr[idx] = max(self.arr[idx*2+1], self.arr[idx*2+2])    
        return

    def query(self, left, right):
        return self.query_(0, 1, self.N, left, right)

    def query_(self, idx, lo, hi, left, right):
        if lo > right or hi < left:
            return 0
        if lo >= left and hi <= right:
            return self.arr[idx]
        mid = (lo + hi)//2
        return max(self.query_(idx*2+1,lo,mid,left,right), self.query_(idx*2+2,mid+1,hi,left,right))


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        candidate = [(s,a) for a,s in zip(ages,scores)]
        candidate.sort()
        res, n = 0, len(candidate)
        # print(candidate)
        tree = SegTree(1000)
        for i in range(n):
            s, a = candidate[i]
            val = tree.query(1,a)
            tree.update(a,val+s)
            # dp[a] = max(dp[j] for j in range(a+1)) + s
            
        return tree.query(1,1000)