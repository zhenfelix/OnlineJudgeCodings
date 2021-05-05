class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(t,i,cost) for i, (t,cost) in enumerate(tasks)]
        heapq.heapify(tasks)
        res, q = [], []
        cur = 0
        while tasks or q:
            if tasks and cur >= tasks[0][0]:
                t, i, cost = heapq.heappop(tasks)
                heapq.heappush(q,(cost,i))
            else:
                if q:
                    cost, i = heapq.heappop(q)
                    res.append(i)
                    cur += cost
                else:
                    cur = tasks[0][0]
        return res 
            