class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def dfs(state, cur):
            if (state, cur) in memo:
                return memo[state, cur]
            
            for bit in range(maxChoosableInteger):
                if state & (1<<bit):
                    if cur + bit + 1 >= desiredTotal or dfs(state - (1<<bit), cur + bit + 1) == False:
                        memo[state, cur] = True
                        return True
            memo[state, cur] = False
            return False
        
        if (1+maxChoosableInteger)*maxChoosableInteger < desiredTotal*2:
            return False
        memo = {}
        return dfs((1<<maxChoosableInteger)-1, 0)