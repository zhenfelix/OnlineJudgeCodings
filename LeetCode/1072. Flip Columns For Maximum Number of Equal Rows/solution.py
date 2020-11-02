class Solution:
    # def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
    #     n, m = len(matrix), len(matrix[0])
    #     res, mp, mask = 0, defaultdict(int), (1<<m) - 1
    #     for i in range(n):
    #         tmp = 0
    #         for j in range(m):
    #             tmp = (tmp<<1) + matrix[i][j]
    #         mp[tmp] += 1
    #         res = max(res,mp[tmp])
    #         tmp ^= mask
    #         mp[tmp] += 1
    #         res = max(res,mp[tmp])
    #     return res

    
    def maxEqualRowsAfterFlips(self, A):
        return max(collections.Counter(tuple(x ^ r[0] for x in r) for r in A).values())