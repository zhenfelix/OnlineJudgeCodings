class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        diff, wsum = [0]*n, [0]*(n+1)
        for i in range(1,n):
            diff[i] += diff[i-1] + (boxes[i][0]!=boxes[i-1][0])
        for i in range(n):
            wsum[i] += wsum[i-1] + boxes[i][-1]
        # print(diff,wsum)
        f, g = [0]*n, [0]*n
        q = deque([-1])
        for i in range(n):
            while q and (i-q[0]>maxBoxes or wsum[i]-wsum[q[0]]>maxWeight):
                q.popleft()
            j = q[0]
            f[i] = g[j]+diff[i]+2
            if i < n-1:
                g[i] = f[i]-diff[i+1]
            while q and g[q[-1]] >= g[i]:
                q.pop()
            q.append(i)
            # print(i,f,g,q)
        return f[-1]



class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        dp, delta, pre = [0]*n, 0, -1
        for cur in range(n):
            maxWeight -= boxes[cur][-1]
            maxBoxes -= 1
            if pre+1 == cur:
                delta += 2
            elif boxes[cur][0] != boxes[cur-1][0]:
                delta += 1
            while maxBoxes < 0 or maxWeight < 0 or (pre < cur-1 and dp[pre] == dp[pre+1]):
                pre += 1
                maxBoxes += 1
                maxWeight += boxes[pre][-1]
                if boxes[pre][0] != boxes[pre+1][0]:
                    delta -= 1
            dp[cur] = dp[pre] + delta
        return dp[-1]
