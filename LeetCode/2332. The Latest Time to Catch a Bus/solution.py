class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers.sort()
        buses.sort()
        ans = -1
        n, m = len(buses), len(passengers)
        j = 0
        for i in range(n):
            cnt = 0
            last = -1
            while j < m and passengers[j] <= buses[i] and cnt < capacity:
                if j == 0 or passengers[j-1] != passengers[j]-1:
                    ans = passengers[j]-1
                last = passengers[j]
                cnt += 1
                j += 1
            if cnt < capacity and last != buses[i]:
                ans = buses[i]
        return ans 

# class Solution:
#     def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
#         passengers.append(float('inf'))
#         s = set(passengers)
#         mx = max(buses)
#         heapq.heapify(buses)
#         cc = Counter()
#         ans = -1
#         for p in sorted(passengers):
#             while buses and (buses[0] < p or cc[buses[0]] == capacity):
#                 heapq.heappop(buses)
#             if not buses:
#                 break
#             cc[buses[0]] += 1
#             ans = p 
#         if cc[mx] < capacity:
#             ans = mx
#         while ans in s:
#             ans -= 1
#         return ans 