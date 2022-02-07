# class Solution:
#     def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
#         candidates = []
#         hs, ss = targetSeconds//60, targetSeconds%60
#         def gen(hs_, ss_):
#             x = hs_*100+ss_
#             tmp = [str(x)]
#             while len(tmp[-1]) < 4:
#                 tmp.append('0'+tmp[-1]) 
#             return tmp

#         if hs < 100:
#             candidates.extend(gen(hs,ss))
#         if ss+60 < 100 and hs-1 >= 0:
#             candidates.extend(gen(hs-1,ss+60))
#         if ss-60 >= 0 and hs+1 < 100:
#             candidates.extend(gen(hs+1,ss-60))

#         def calc(mv):
#             cost = 0
#             pre = str(startAt)
#             for ch in mv:
#                 if ch != pre:
#                     pre = ch
#                     cost += moveCost
#             return cost+len(mv)*pushCost

#         # print([(x,calc(x)) for x in candidates])
#         return min(calc(x) for x in candidates)

class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        candidates = []
        hs, ss = targetSeconds//60, targetSeconds%60
        def gen(hs_, ss_):
            x = hs_*100+ss_
            return str(x)

        if hs < 100:
            candidates.append(gen(hs,ss))
        if ss+60 < 100 and hs-1 >= 0:
            candidates.append(gen(hs-1,ss+60))
        if ss-60 >= 0 and hs+1 < 100:
            candidates.append(gen(hs+1,ss-60))

        def calc(mv):
            cost = 0
            pre = str(startAt)
            for ch in mv:
                if ch != pre:
                    pre = ch
                    cost += moveCost
            return cost+len(mv)*pushCost

        # print([(x,calc(x)) for x in candidates])
        return min(calc(x) for x in candidates)

