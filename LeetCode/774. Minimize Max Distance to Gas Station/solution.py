# class Solution:
#     """
#     @param stations: an integer array
#     @param k: an integer
#     @return: the smallest possible value of D
#     """
#     def minmaxGasDist(self, stations, k):
#         # Write your code here
#         epsilon = 1e-7
#         stations = [num-stations[i-1] for i,num in enumerate(stations) if i>0]
#         def isLess(target):
#             cc = 0
#             for s in stations:
#                 if s > target:
#                     tmp = s//target
#                     if tmp*target == s:
#                         tmp -= 1
#                     cc += tmp
#                     if cc > k:
#                         return True
#             return False

#         lo, hi = 0, max(stations)
#         while lo + epsilon < hi:
#             mid = (lo + hi)/2
#             if isLess(mid):
#                 lo = mid 
#             else:
#                 hi = mid

#         return hi



class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        lo, hi = 0, 10**8
        while hi-lo >= 10**-6:
            mid = (lo+hi)/2
            cnt = 0
            for a, b in zip(stations[:-1],stations[1:]):
                cnt += (b-a)//mid
                if cnt > k:
                    break
            if cnt > k:
                lo = mid 
            else:
                hi = mid 
        return (lo+hi)/2


class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        lo, hi, delta = 0, stations[-1]-stations[0], 1e-6
        distances = [b-a for a,b in zip(stations,stations[1:])]
        while lo + delta <= hi:
            mid = (lo+hi)/2
            # print(lo,hi,mid)
            cnt = 0
            for dis in distances:
                cnt += dis//mid - (dis%mid == 0)
                if cnt > K:
                    break
            if cnt > K:
                lo = mid
            else:
                hi = mid
        return hi

