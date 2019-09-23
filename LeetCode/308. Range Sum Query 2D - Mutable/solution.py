# class NumMatrix:

#     def __init__(self, matrix: List[List[int]]):
#         if not matrix: return
#         n, m = len(matrix), len(matrix[0])
#         N = max(n,m)
#         tree = [0]*(N*N*8)
#         def build(row_lo, col_lo, row_hi, col_hi, idx):
#             sums = 0
#             if row_lo > row_hi or col_lo > col_hi:
#                 return 0
#             elif row_lo == row_hi and col_lo == col_hi:
#                 sums += matrix[row_lo][col_lo]
#             else:
#                 row_mid = (row_lo+row_hi)//2
#                 col_mid = (col_lo+col_hi)//2
#                 sums += build(row_lo, col_lo, row_mid, col_mid, idx*4+1)
#                 sums += build(row_lo, col_mid+1, row_mid, col_hi, idx*4+2)
#                 sums += build(row_mid+1, col_lo, row_hi, col_mid, idx*4+3)
#                 sums += build(row_mid+1, col_mid+1, row_hi, col_hi, idx*4+4)
#             tree[idx] = sums
#             # print(row_lo, col_lo, row_hi, col_hi, idx, tree[idx])
#             return tree[idx]
#         build(0,0,n-1,m-1,0)
#         self.tree = tree
#         self.n, self.m = n, m
#         self.matrix = matrix
#         # print(self.tree)
#         return
            
        

#     def update(self, row: int, col: int, val: int) -> None:
#         delta = val - self.matrix[row][col]
#         self.matrix[row][col] = val
#         def update_(row_lo, col_lo, row_hi, col_hi, idx):
#             if row_lo > row_hi or col_lo > col_hi or row_hi < row or row_lo > row or col_hi < col or col_lo > col:
#                 return
#             elif row_lo == row_hi and col_lo == col_hi:
#                 pass
#             else:
#                 row_mid = (row_lo+row_hi)//2
#                 col_mid = (col_lo+col_hi)//2
#                 update_(row_lo, col_lo, row_mid, col_mid, idx*4+1)
#                 update_(row_lo, col_mid+1, row_mid, col_hi, idx*4+2)
#                 update_(row_mid+1, col_lo, row_hi, col_mid, idx*4+3)
#                 update_(row_mid+1, col_mid+1, row_hi, col_hi, idx*4+4)
#             self.tree[idx] += delta
#             return
#         update_(0,0,self.n-1,self.m-1,0)
#         return

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         def query(row_lo, col_lo, row_hi, col_hi, idx):
#             sums = 0
#             if row_lo > row_hi or col_lo > col_hi or row_hi < row1 or row_lo > row2 or col_hi < col1 or col_lo > col2:
#                 return 0
#             elif row_lo >= row1 and row_hi <= row2 and col_lo >= col1 and col_hi <= col2:
#                 sums = self.tree[idx]
#             else:
#                 row_mid = (row_lo+row_hi)//2
#                 col_mid = (col_lo+col_hi)//2
#                 sums += query(row_lo, col_lo, row_mid, col_mid, idx*4+1)
#                 sums += query(row_lo, col_mid+1, row_mid, col_hi, idx*4+2)
#                 sums += query(row_mid+1, col_lo, row_hi, col_mid, idx*4+3)
#                 sums += query(row_mid+1, col_mid+1, row_hi, col_hi, idx*4+4)
#             return sums
#         return query(0,0,self.n-1,self.m-1,0)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix: return
        n, m = len(matrix), len(matrix[0])
        N = max(n,m)
        tree = [[0]*(N*4) for _ in range(N*4)]
        # print(tree)

        def build(row_lo, col_lo, row_hi, col_hi, row_idx, col_idx):
            sums = 0
            # print(row_lo, col_lo, row_hi, col_hi, row_idx, col_idx, tree[row_idx][col_idx])
            if row_lo > row_hi or col_lo > col_hi:
                return 0
            elif row_lo == row_hi and col_lo == col_hi:
                sums += matrix[row_lo][col_lo]
            else:
                row_mid = (row_lo + row_hi) // 2
                col_mid = (col_lo + col_hi) // 2
                sums += build(row_lo, col_lo, row_mid, col_mid, row_idx*2+1, col_idx*2+1)
                sums += build(row_lo, col_mid + 1, row_mid, col_hi, row_idx*2+1, col_idx*2+2)
                sums += build(row_mid + 1, col_lo, row_hi, col_mid, row_idx*2+2, col_idx*2+1)
                sums += build(row_mid + 1, col_mid + 1, row_hi, col_hi, row_idx*2+2, col_idx*2+2)
            tree[row_idx][col_idx] = sums
            # print(row_lo, col_lo, row_hi, col_hi, row_idx, col_idx, tree[row_idx][col_idx])
            return tree[row_idx][col_idx]

        build(0, 0, n - 1, m - 1, 0, 0)
        self.tree = tree
        self.n, self.m = n, m
        self.matrix = matrix
        # print(self.tree)
        return

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val

        def update_(row_lo, col_lo, row_hi, col_hi, row_idx, col_idx):
            if row_lo > row_hi or col_lo > col_hi or row_hi < row or row_lo > row or col_hi < col or col_lo > col:
                return
            elif row_lo == row_hi and col_lo == col_hi:
                pass
            else:
                row_mid = (row_lo + row_hi) // 2
                col_mid = (col_lo + col_hi) // 2
                update_(row_lo, col_lo, row_mid, col_mid, row_idx*2+1, col_idx*2+1)
                update_(row_lo, col_mid + 1, row_mid, col_hi, row_idx*2+1, col_idx*2+2)
                update_(row_mid + 1, col_lo, row_hi, col_mid, row_idx*2+2, col_idx*2+1)
                update_(row_mid + 1, col_mid + 1, row_hi, col_hi, row_idx*2+2, col_idx*2+2)
            self.tree[row_idx][col_idx] += delta
            return

        update_(0, 0, self.n - 1, self.m - 1, 0, 0)
        return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def query(row_lo, col_lo, row_hi, col_hi, row_idx, col_idx):
            sums = 0
            if row_lo > row_hi or col_lo > col_hi or row_hi < row1 or row_lo > row2 or col_hi < col1 or col_lo > col2:
                return 0
            elif row_lo >= row1 and row_hi <= row2 and col_lo >= col1 and col_hi <= col2:
                sums = self.tree[row_idx][col_idx]
            else:
                row_mid = (row_lo + row_hi) // 2
                col_mid = (col_lo + col_hi) // 2
                sums += query(row_lo, col_lo, row_mid, col_mid, row_idx*2+1, col_idx*2+1)
                sums += query(row_lo, col_mid + 1, row_mid, col_hi, row_idx*2+1, col_idx*2+2)
                sums += query(row_mid + 1, col_lo, row_hi, col_mid, row_idx*2+2, col_idx*2+1)
                sums += query(row_mid + 1, col_mid + 1, row_hi, col_hi, row_idx*2+2, col_idx*2+2)
            return sums

        return query(0, 0, self.n - 1, self.m - 1, 0, 0)