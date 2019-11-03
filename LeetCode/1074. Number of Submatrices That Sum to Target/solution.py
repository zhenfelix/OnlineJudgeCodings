class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(1,m):
                matrix[i][j] += matrix[i][j-1]
        res = 0
        for left in range(m):
            for right in range(left,m):
                cc, presum = collections.Counter(), 0
                cc[presum] += 1
                for r in range(n):
                    cur = matrix[r][right] - (0 if left == 0 else matrix[r][left-1])
                    presum += cur
                    res += cc[presum-target]
                    cc[presum] += 1
        return res
    

