class Solution:
    def numFlowers(self, roads: List[List[int]]) -> int:
        cc = Counter()
        cnt = 1
        for a, b in roads:
            cc[a] += 1
            cc[b] += 1
            cnt = max(cnt, cc[a]+1, cc[b]+1)
        return cnt