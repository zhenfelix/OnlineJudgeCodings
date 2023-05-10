class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        start = tuple(start)
        target = tuple(target)
        points = set([start,target])
        costs = dict()
        
        for x1,y1,x2,y2,c in specialRoads:
            points.add((x1,y1))
            points.add((x2,y2))
        points = list(points)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                # if i == j: continue
                x2, y2 = points[j]
                costs[x1,y1,x2,y2] = abs(x1-x2)+abs(y1-y2)
        for x1,y1,x2,y2,c in specialRoads:
            costs[x1,y1,x2,y2] = min(costs[x1,y1,x2,y2],c)

        
        hq = [(0,start)]
        dist = dict()
        for x2, y2 in points:
            dist[(x2,y2)] = inf 
        dist[start] = 0
        while hq:
            d, cur = heappop(hq)
            if cur == target: return d 
            if d > dist[cur]: continue
            for nxt in points:
                if d+costs[cur[0],cur[1],nxt[0],nxt[1]] < dist[nxt]:
                    dist[nxt] = d+costs[cur[0],cur[1],nxt[0],nxt[1]]
                    heappush(hq,(dist[nxt],nxt))
        return -1