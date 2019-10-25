# import heapq

# class Solution:
#     def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
#         hs = []
#         coordinates = []
#         res = []
#         passed = set()
#         for i, building in enumerate(buildings):
#             coordinates.append((building[0],-i-1))
#             coordinates.append((building[1],i+1))
#         coordinates = sorted(coordinates)
#         h = 0
#         # print(coordinates)
#         for i, coordinate in enumerate(coordinates):
#             x, idx = coordinate[0], coordinate[1]
#             # print(x,idx,h)
#             # print(hs)
#             if idx < 0:
#                 heapq.heappush(hs,(-buildings[-idx-1][2],-idx))
#             else:
#                 passed.add(idx)
#             while hs and hs[0][-1] in passed:
#                 heapq.heappop(hs)
#             if i+1 < len(coordinates) and x == coordinates[i+1]:
#                 continue
#             if hs and h != -hs[0][0]:
#                 # if res and x == res[-1][0]:
#                 #     if idx < 0:
#                 #         h = max(res[-1][-1], -hs[0][0])
#                 #         res[-1][-1] = h
#                 #     else:
#                 #         h = min(res[-1][-1], -hs[0][0])
#                 #         res[-1][-1] = h
#                 # else:
#                 #     h = -hs[0][0]
#                 #     res.append([x,h])

#                 h = -hs[0][0]
#                 res.append([x,h])
                
#             elif not hs:
#                 h = 0
#                 # if res and x == res[-1][0]:
#                 #     res[-1][-1] = 0
#                 # else:
#                 #     res.append([x,h])
#                 res.append([x,h])
#         return res


from heapq import heappush, heappop
class Solution(object):
    def getSkyline(self, buildings):
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        # the building with higher height become active first in case several buildings with the same left position
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()

        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            # 2, if it's the start-building event, make the building alive
            # 3, if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos: heappop(live)
            if negH: heappush(live, (negH, R))
            if res[-1][1] != -live[0][0]:
                res += [ [pos, -live[0][0]] ]
        return res[1:]