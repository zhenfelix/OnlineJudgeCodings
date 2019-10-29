import itertools
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        
        def dfs(i, j):
            if (i,j) in memo:
                return memo[i,j]
            if i == j:
                memo[i,j] = [(nums_[i],1)]
                return memo[i,j]
            memo[i,j] = []
            for k in range(i+1,j+1):
                left, right = dfs(i,k-1), dfs(k,j)
                memo[i,j] += [(l[0]*r[0],l[1]*r[1]) for l in left for r in right]
                memo[i,j] += [(l[0]*r[1],l[1]*r[0]) for l in left for r in right]
                memo[i,j] += [(l[0]*r[1]+r[0]*l[1],l[1]*r[1]) for l in left for r in right]
                memo[i,j] += [(l[0]*r[1]-r[0]*l[1],l[1]*r[1]) for l in left for r in right]
            return memo[i,j]


        p = itertools.permutations(nums)
        for nums_ in p:
            # print(nums_)
            memo = {}
            dfs(0,3)
            # print(memo[0,3])
            for p, q in memo[0,3]:
                if q != 0 and 24 * q == p:
                    # print(p,q)
                    return True

        return False


