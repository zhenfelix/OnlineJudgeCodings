class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        def check(t):
            # print(t)
            arr = stations[:]
            cnt = 0
            remains = k 
            for i in range(min(r,n)):
                cnt += arr[i]
            for i in range(n):
                right = i+r  
                left = i-r-1
                if right < n:
                    cnt += arr[right]
                if left >= 0:
                    cnt -= arr[left]
                if cnt < t:
                    delta = t-cnt
                    remains -= delta
                    if remains < 0:
                        return False
                    arr[min(right,n-1)] += delta
                    cnt = t 
                # print(arr)
            return True

        lo, hi = min(stations), sum(stations)+k 
        while lo <= hi:
            m = (lo+hi)//2
            if check(m):
                lo = m + 1
            else:
                hi = m - 1
        return hi

