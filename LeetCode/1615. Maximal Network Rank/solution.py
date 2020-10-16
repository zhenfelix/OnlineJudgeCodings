class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        res = 0
        edges = set()
        degree = Counter()
        for a, b in roads:
            edges.add((a,b))
            edges.add((b,a))
            degree[a] += 1
            degree[b] += 1
        for i in range(n):
            for j in range(i+1,n):
                res = max(res, degree[i]+degree[j]-((i,j) in edges))
        return res