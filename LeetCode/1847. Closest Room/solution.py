from sortedcontainers import SortedList

class Solution:
    def closestRoom(self, rooms, queries):
        Q = sorted([(y, x, i) for i, (x,y) in enumerate(queries)])[::-1]
        R = sorted((y, x) for x, y in rooms)[::-1]
        n, q = len(R), len(Q)
        p1, p2, aval, ans = 0, 0, SortedList(), [-1]*q

        while p1 <= n and p2 < len(Q):
            if p1 < n and R[p1][0] >= Q[p2][0]:
                aval.add(R[p1][1])
                p1 += 1
            else:
                if len(aval) != 0:
                    preferred, ind = Q[p2][1], Q[p2][2]
                    i = aval.bisect(preferred)
                    
                    cands = []
                    if i > 0: cands.append(aval[i-1])
                    if i < len(aval): cands.append(aval[i])
                    ans[ind] = min(cands, key = lambda x: abs(x - preferred))

                p2 += 1

        return ans


# class Solution:
#     def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
#         rooms.sort(key=lambda x: x[1], reverse=True)  # Sort by decreasing order of room size
#         qArr = []  # zip query with its index
#         for i, q in enumerate(queries):
#             qArr.append((i, q))
#         qArr.sort(key=lambda x: x[1][1], reverse=True)  # Sort by decreasing order of query minSize

#         def searchGreaterOrEqual(arr, x):
#             left = 0
#             right = len(arr) - 1
#             ans = -1
#             while left <= right:
#                 mid = left + (right - left) // 2
#                 if arr[mid] >= x:
#                     ans = mid
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             return ans

#         def searchLessOrEqual(arr, x):
#             left = 0
#             right = len(arr) - 1
#             ans = -1
#             while left <= right:
#                 mid = left + (right - left) // 2
#                 if arr[mid] <= x:
#                     ans = mid
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return ans

#         def searchClosestRoomId(arr, x):
#             ansAbs = math.inf
#             ans = -1
#             i1 = searchLessOrEqual(arr, x)
#             if i1 != -1:
#                 ansAbs = abs(x - arr[i1])
#                 ans = arr[i1]
#             i2 = searchGreaterOrEqual(arr, x)
#             if i2 != -1 and ansAbs > abs(x - arr[i2]):
#                 ans = arr[i2]
#             return ans

#         sortedRoomIdsSoFar = []  # Room id is sorted in
#         n, k = len(rooms), len(queries)
#         i = 0
#         ans = [-1] * k
#         for index, q in qArr:
#             while i < n and rooms[i][1] >= q[1]:
#                 bisect.insort(sortedRoomIdsSoFar, rooms[i][0])  # Add id of the room which its size >= query minSize
#                 i += 1
#             ans[index] = searchClosestRoomId(sortedRoomIdsSoFar, q[0])
#         return ans