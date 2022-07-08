class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cc = [0]*n 
        for u, v in roads:
            cc[u] += 1
            cc[v] += 1
        tot = 0
        for i, c in enumerate(sorted(cc)):
            tot += c*(i+1)
        return tot