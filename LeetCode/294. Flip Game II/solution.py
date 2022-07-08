# 10170 Sprague-Grundy定理是怎么想出来的
# https://zhuanlan.zhihu.com/p/20611132

def mex(sgs):
    cur = 0
    while True:
        if cur not in sgs:
            return cur 
        cur += 1
    return -1

N = 61
dp = [0]*N 
for i in range(2,N):
    left, right = 0, i-2
    sgs = set()
    while left <= right:
        sgs.add(dp[left]^dp[right])
        left += 1
        right -= 1
    dp[i] = mex(sgs)
# print(dp)

class Solution:
    def canWin(self, currentState: str) -> bool:
        ans, cnt = 0, 0
        currentState += '-'
        for ch in currentState:
            if ch == '-':
                if cnt > 0:
                    ans ^= dp[cnt]
                    cnt = 0
            else:
                cnt += 1

        return ans > 0


# TLE "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
class Solution:
    def canWin(self, currentState: str) -> bool:
        n = len(currentState)
        s = 0
        for ch in currentState:
            s <<= 1
            if ch == '+':
                s |= 1
        @cache
        def dfs(cur):
            mask = 3
            for i in range(n-1):
                if (cur&mask) == mask and dfs(cur^mask) == False:
                    return True
                mask <<= 1
            return False
        return dfs(s)


# class Solution:
#     def canWin(self, s: str) -> bool:
#         def dfs(state):
#             if state in memo:
#                 return memo[state]
#             n = len(state)
#             for i in range(n-1):
#                 if state[i] == state[i+1] == '+' and dfs(state[:i]+"--"+state[i+2:]) == False:
#                     memo[state] = True
#                     return True
#             memo[state] = False
#             return False
        
#         memo = {}
#         return dfs(s)