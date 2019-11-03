class Leaderboard(object):

    def __init__(self):
        self.A = collections.Counter()

    def addScore(self, playerId, score):
        self.A[playerId] += score

    def top(self, K):
        return sum(v for i,v in self.A.most_common(K))

    def reset(self, playerId):
        self.A[playerId] = 0


# import heapq
# class Leaderboard:

#     def __init__(self):
#         self.heap = []
#         self.mp = collections.Counter()

#     def addScore(self, playerId: int, score: int) -> None:
#         self.mp[playerId] += score
#         heapq.heappush(self.heap,(-self.mp[playerId], playerId))
                

#     def top(self, K: int) -> int:
#         sums, cnt = 0, 0
#         tmp = []
#         while cnt < K:
#             v, pid = heapq.heappop(self.heap)
#             if self.mp[pid] == -v:
#                 sums -= v
#                 cnt += 1
#                 tmp.append((v,pid))
#         for x in tmp:
#             heapq.heappush(self.heap,x)
#         return sums

        

#     def reset(self, playerId: int) -> None:
#         self.mp[playerId] = 0
        


# # Your Leaderboard object will be instantiated and called as such:
# # obj = Leaderboard()
# # obj.addScore(playerId,score)
# # param_2 = obj.top(K)
# # obj.reset(playerId)