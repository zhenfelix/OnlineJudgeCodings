class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        from collections import defaultdict
        row_seen, col_seen = defaultdict(lambda: 0), defaultdict(lambda: 0)
        for row, col in indices:
            row_seen[row] += 1
            col_seen[col] += 1
        row_incr = len([1 for _, count in row_seen.items() if count % 2 == 1 ])
        col_incr = len([1 for _, count in col_seen.items() if count % 2 == 1 ])
        return row_incr * m + col_incr * n  - row_incr * col_incr * 2
    # def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # odd_count = 0
        # rows = [0] * n
        # cols = [0] * m
        # for i, j in indices:
        #     rows[i] = rows[i] ^ 1
        #     cols[j] = cols[j] ^ 1
        # for i in range(n):
        #     for j in range(m):
        #         if(rows[i] ^ cols[j] == 1): odd_count += 1
        # return odd_count

