from collections import deque

class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        q = deque()
        q.append((0,1))
        # dp = {}
        # dp[0,1] = 0
        visited = set()
        visited.add((0,1))
        step = 0
        while q:
            n = len(q)
            for _ in range(n):
                distance, speed = q.popleft()
                if distance == target:
                    return step
                if distance+speed > 0 and distance+speed < 2*target:
                # if (distance+speed,speed*2) not in dp and distance+speed > 0 and distance+speed < 2*target:
                    # dp[distance+speed,speed*2] = dp[distance,speed]+1
                    # if distance+speed == target:
                    #     return dp[target,speed*2]
                    q.append((distance+speed,speed*2))
                if (distance,speed//abs(speed)*(-1)) not in visited:
                # if (distance,speed//abs(speed)*(-1)) not in dp:
                    # dp[distance,speed//abs(speed)*(-1)] = dp[distance,speed]+1
                    visited.add((distance,speed//abs(speed)*(-1)))
                    q.append((distance,speed//abs(speed)*(-1)))
            step += 1
        return -1


# from collections import deque

# class Solution(object):
#     def racecar(self, target):
#         """
#         :type target: int
#         :rtype: int
#         """
#         q = deque()
#         dp = {}
#         n = target.bit_length()
#         if 1<<n == target+1:
#             return n
#         distance, speed = 0, 1
#         for i in range(n):
#             dp[distance,speed] = i 
#             q.append((distance,speed))
#             distance += speed
#             speed *= 2
#         while q:
#             distance, speed = q.popleft()
#             if distance == target:
#                 return dp[distance,speed]
#             # if distance+speed > 0 and distance+speed < 2*target:
#             if (distance+speed,speed*2) not in dp and distance+speed > 0 and distance+speed < 2*target:
#                 dp[distance+speed,speed*2] = dp[distance,speed]+1
#                 # if distance+speed == target:
#                 #     return dp[target,speed*2]
#                 q.append((distance+speed,speed*2))
#             # if (distance,speed//abs(speed)*(-1)) not in visited:
#             if (distance,speed//abs(speed)*(-1)) not in dp:
#                 dp[distance,speed//abs(speed)*(-1)] = dp[distance,speed]+1
#                 # visited.add((distance,speed//abs(speed)*(-1)))
#                 q.append((distance,speed//abs(speed)*(-1)))
#         return -1


# import functools

class Solution(object):
    # @functools.lru_cache(None)
    def racecar(self, target):
        def dfs(t):
            if t in dp:
                return dp[t]
            n = t.bit_length()
            if 1<<n == t+1:
                dp[t] = n
                return n
            res = float('inf')
            for i in range(n):
                for j in range(i):
                    res = min(res, i+j+2+dfs(t-((1<<i)-(1<<j))))
            res = min(res, n+1+dfs((1<<n)-(t+1)))
            dp[t] = res
            return res
        dp = {}
        return dfs(target)

        
