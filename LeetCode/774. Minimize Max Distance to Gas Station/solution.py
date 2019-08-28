class Solution:
    """
    @param stations: an integer array
    @param k: an integer
    @return: the smallest possible value of D
    """
    def minmaxGasDist(self, stations, k):
        # Write your code here
        epsilon = 1e-7
        stations = [num-stations[i-1] for i,num in enumerate(stations) if i>0]
        def isLess(target):
            cc = 0
            for s in stations:
                if s > target:
                    tmp = s//target
                    if tmp*target == s:
                        tmp -= 1
                    cc += tmp
                    if cc > k:
                        return True
            return False

        lo, hi = 0, max(stations)
        while lo + epsilon < hi:
            mid = (lo + hi)/2
            if isLess(mid):
                lo = mid 
            else:
                hi = mid

        return hi
