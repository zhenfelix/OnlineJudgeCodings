class Solution:
    def canWin(self, s: str) -> bool:
        def dfs(state):
            if state in memo:
                return memo[state]
            n = len(state)
            for i in range(n-1):
                if state[i] == state[i+1] == '+' and dfs(state[:i]+"--"+state[i+2:]) == False:
                    memo[state] = True
                    return True
            memo[state] = False
            return False
        
        memo = {}
        return dfs(s)