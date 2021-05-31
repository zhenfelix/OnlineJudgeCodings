class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n, m = len(servers), len(tasks)
        q = []
        ready = [(w,i) for i, w in enumerate(servers)]
        heapq.heapify(ready)
        ans = [-1]*m 
        start = 0
        for i in range(m):
            start = max(start, i) 
            if not ready:
                start = q[0][0]
            while q and start >= q[0][0]:
                _, w, idx = heapq.heappop(q)
                heapq.heappush(ready, (w,idx))
            w, idx = heapq.heappop(ready)
            ans[i] = idx
            heapq.heappush(q, (start+tasks[i], w, idx))
        return ans