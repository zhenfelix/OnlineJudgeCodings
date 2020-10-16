class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x0, y0 = location
        ans = ovlp = 0
        theta = [] 
        for x, y in points: 
            if x == x0 and y == y0: ovlp += 1
            else: theta.append(atan2(y-y0, x-x0)) # (x, y) wrt (x0, y0)
        
        theta.sort()
        theta += [x+2*pi for x in theta]
        ii = 0
        for i in range(len(theta)): 
            while theta[i] - theta[ii] > angle*pi/180: ii += 1
            ans = max(ans, i-ii+1)
        return ans + ovlp


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        arr = []
        pi = 3.141592653589793
        epsilon = 0.000001
        res, base = 0, 0
        for x, y in points:
            if x == location[0] and y == location[1]:
                base += 1
                continue
            cur = atan2(y-location[1],x-location[0])
            cur = cur/pi*180
            arr.append(cur)
        arr.sort()
        # print(arr)
        q = deque()
        for a in arr:
            q.append(a)
            while q and q[-1]-q[0] > angle + epsilon:
                q.popleft()
            res = max(res,len(q))
        for a in arr:
            q.append(a+360)
            while q and q[-1]-q[0] > angle + epsilon:
                q.popleft()
            res = max(res,len(q))
        return res + base