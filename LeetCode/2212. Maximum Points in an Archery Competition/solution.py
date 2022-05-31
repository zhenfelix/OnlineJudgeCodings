from functools import lru_cache
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:

        @lru_cache(None)
        def dfs(i, cnt):
            if cnt < 0:
                return -float('inf')
            if i < 0:
                return 0
            return max(i+dfs(i-1,cnt-aliceArrows[i]-1), dfs(i-1,cnt))
        n = len(aliceArrows)
        dfs(n-1, numArrows)
        bobArrows = [0]*n
        for i in range(n)[::-1]:
            if i+dfs(i-1,numArrows-aliceArrows[i]-1) >= dfs(i-1, numArrows):
                bobArrows[i] = aliceArrows[i]+1
                numArrows -= bobArrows[i]
        if numArrows > 0:
            bobArrows[0] += numArrows
        return bobArrows


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:

        n = len(aliceArrows)
        best_score, best_state = 0, -1
        for s in range(1<<n):
            score = 0
            remains = numArrows
            for i in range(n):
                if (s>>i)&1:
                    score += i
                    remains -= (aliceArrows[i]+1)
                if remains < 0:
                    break
            if remains >= 0 and score > best_score:
                best_score = score
                best_state = s 

        bobArrows = [0]*n
        # print(bin(best_state), best_score)
        for i in range(n):
            if (best_state>>i)&1:
                bobArrows[i] += (aliceArrows[i]+1)
                numArrows -= bobArrows[i]
        bobArrows[-1] += numArrows
        return bobArrows