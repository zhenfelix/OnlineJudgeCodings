class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        cc = Counter()
        for u, v in edges:
            if cc[u]:
                return u
            if cc[v]:
                return v
            cc[u] += 1
            cc[v] += 1
        return -1