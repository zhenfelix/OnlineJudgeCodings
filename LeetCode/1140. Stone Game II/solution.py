import math
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        sums = 0
        for s in piles:
            sums += s
        memo = {}
        def dfs(idx, M, flag):
            if idx >= n:
                return 0
            if (idx,M,flag) in memo:
                return memo[idx,M,flag]
            
            if flag:
                score = -math.inf
                start = idx
                s = 0
                while start < n and start < idx+2*M:
                    s += piles[start]
                    score = max(score,s+dfs(start+1,max(M,start-idx+1),not flag))
                    start += 1
                # print(score)
                
            else:
                score = math.inf
                start = idx
                s = 0
                while start < n and start < idx+2*M:
                    s -= piles[start]
                    score = min(score,s+dfs(start+1,max(M,start-idx+1),not flag))
                    start += 1

            memo[idx,M,flag] = score
            return score
            
        ans = dfs(0,1,True)
        ans += sums
        return ans//2