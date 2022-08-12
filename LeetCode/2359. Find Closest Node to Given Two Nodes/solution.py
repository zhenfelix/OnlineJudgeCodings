class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        def doit(cur):
            dist = [inf]*n 
            cnt = 0
            while cur != -1 and dist[cur] == inf:
                dist[cur] = cnt
                cur = edges[cur]
                cnt += 1  
            return dist
        dist1 = doit(node1)
        dist2 = doit(node2)
        ans = [-1, inf]
        for i in range(n):
            tmp = max(dist1[i],dist2[i])
            if tmp < ans[-1]:
                ans = [i, tmp]
        return ans[0]
                

