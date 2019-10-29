class Solution:
    # def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp = collections.defaultdict(int)
        # dp[0,0] = poured
        # for i in range(query_row+1):
        #     for j in range(i+1):
        #         exceeded = (dp[i,j] - 1)/2
        #         if exceeded < 0: exceeded = 0
        #         dp[i,j] -= exceeded*2
        #         dp[i+1,j] += exceeded
        #         dp[i+1,j+1] += exceeded
        # return dp[query_row,query_glass]
        
    def champagneTower(self, poured, query_row, query_glass):
        res = [poured] + [0] * query_row
        for row in range(1, query_row + 1):
            for i in range(row, -1, -1):
                res[i] = max(res[i] - 1, 0) / 2.0 + max(res[i - 1] - 1, 0) / 2.0
        return min(res[query_glass], 1)