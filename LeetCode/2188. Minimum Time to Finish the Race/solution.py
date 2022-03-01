class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        n = len(tires)
        cost = []
        curs = [f for f, r in tires]
        for i in range(20):
            cost.append(min(curs))
            for j in range(n):
                curs[j] += tires[j][0]*tires[j][1]
                tires[j][0] *= tires[j][1]
                if curs[j] > 10**6:
                    curs[j] = float('inf')
                if tires[j][0] > 10**6:
                    tires[j][0] = float('inf')
        # print(cost)
        dp = [float('inf')]*numLaps
        dp[0] = cost[0]
        for i in range(1,numLaps):
            if i < 20:
                dp[i] = cost[i]
            for j in range(max(0,i-20),i):
                dp[i] = min(dp[i], changeTime+cost[i-j-1]+dp[j])
        # print(dp)
        return dp[-1]



K = 20

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        inf = 10**6
        best = [float('inf')] * (K + 1)
        for f, r in tires:
            lap, last, tot = 1, f, f
            while lap <= K and tot < inf:
                best[lap] = min(best[lap], tot)
                lap, last, tot = lap + 1, last * r, tot + last * r
            
        dp = [float('inf')] * (numLaps + 1)
        dp[0] = 0
        for i in range(1, numLaps + 1):
           
            for j in range(max(0, i - K), i):
                dp[i] = min(dp[i], dp[j] + changeTime + best[i - j])
                
        return dp[numLaps] - changeTime


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/eU8bPl/view/rUilTq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。