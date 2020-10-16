class Solution:
#     def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
#         stations = [[0,startFuel]] + sorted(stations)
#         n = len(stations)        
#         reach = [-float('inf')]*n
#         reach[0] = startFuel
#         st = [startFuel]*n
#         flag = True
#         cnt = 0
#         if target <= startFuel:
#             return 0
#         while flag:
#             flag = False
#             cnt += 1
#             for i in range(1,len(reach))[::-1]:
#                 p, g = stations[i]
#                 st.pop()
#                 if p <= st[-1] and st[-1] + g > reach[i]:
#                     reach[i] = st[-1] + g
#                     flag = True
#                     if reach[i] >= target:
#                         return cnt
#             for i in range(1,len(reach)):
#                 st.append(max(st[-1],reach[i]))
            
#         return -1


    # def minRefuelStops(self, target, startFuel, s):
    #     dp = [startFuel] + [0] * len(s)
    #     for i in range(len(s)):
    #         for t in range(i + 1)[::-1]:
    #             if dp[t] >= s[i][0]:
    #                 dp[t + 1] = max(dp[t + 1], dp[t] + s[i][1])
    #     for t, d in enumerate(dp):
    #         if d >= target: return t
    #     return -1
    
    def minRefuelStops(self, target, reach, s):
        pq = []
        cnt = cur = 0
        while reach < target:
            while cur < len(s) and s[cur][0] <= reach:
                heapq.heappush(pq, -s[cur][1])
                cur += 1
            if not pq: return -1
            reach += -heapq.heappop(pq)
            cnt += 1
        return cnt