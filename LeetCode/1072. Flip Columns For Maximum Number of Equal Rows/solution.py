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

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        res = 0
        cc = defaultdict(int)
        for i in range(n):
            s = [0]
            for j in range(1,m):
                if matrix[i][0] == 0:
                    s.append(matrix[i][j])
                else:
                    s.append(1-matrix[i][j])
            cc[''.join(map(str,s))] += 1
        return max(cc.values())


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        res = 0
        cc = defaultdict(int)
        trie = [[-1]*2 for _ in range(n*m+10)]
        tot = 1
        for i in range(n):
            cur = 0
            for j in range(m):
                ch = matrix[i][j]^matrix[i][0]
                if trie[cur][ch] == -1:
                    trie[cur][ch] = tot
                    tot += 1
                cur = trie[cur][ch]

            cc[cur] += 1
        return max(cc.values())