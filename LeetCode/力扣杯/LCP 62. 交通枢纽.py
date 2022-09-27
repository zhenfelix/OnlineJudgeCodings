class Solution:
    def transportationHub(self, path: List[List[int]]) -> int:
        indegree = defaultdict(set)
        outdegree = defaultdict(set)
        points = set()
        for a, b in path:
            points.add(a)
            points.add(b)
            outdegree[a].add(b)
            indegree[b].add(a)
        n = len(points)
        for p in points:
            if len(outdegree[p]) == 0 and len(indegree[p]) == n-1:
                return p 
        return -1
