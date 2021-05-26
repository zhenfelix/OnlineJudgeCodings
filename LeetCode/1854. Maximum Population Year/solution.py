class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        delta = defaultdict(int)
        for a, b in logs:
            delta[a] += 1
            delta[b] -= 1
        cur, res, year = 0, 0, -1
        for x in range(1950,2051,1):
            # print(x)
            cur += delta[x]
            if cur > res:
                res = cur
                year = x
        return year