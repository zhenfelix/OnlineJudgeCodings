class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        n = len(temperatureA)
        cnt, ans = 0, 0
        for i in range(1,n):
            a = temperatureA[i]-temperatureA[i-1]
            b = temperatureB[i]-temperatureB[i-1]
            if (a == b == 0) or (a > 0 and b > 0) or (a < 0 and b < 0):
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans
