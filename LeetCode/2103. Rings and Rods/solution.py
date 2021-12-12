class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        n //= 2
        st = defaultdict(set)
        for i in range(n):
            st[int(rings[i*2+1])].add(rings[i*2])
        return sum(len(st[i]) == 3 for i in range(10))
