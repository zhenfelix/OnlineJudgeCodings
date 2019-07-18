class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*n
        for v in bookings:
            ans[v[0]-1] += v[2]
            if v[1] < n:
                ans[v[1]] -= v[2]
        for i in range(1,n):
            ans[i] += ans[i-1]
        return ans
            