
# class Solution:
#     def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
#         rows, cols, diags, anti_diags = Counter(), Counter(), Counter(), Counter()
#         seen = set()
#         for r, c in lamps:
#             rows[r] += 1
#             cols[c] += 1
#             diags[r-c] += 1
#             anti_diags[r+c] += 1
#             seen.add((r,c))
#         # for i in range(len(rows)):
#         #     print(rows[i])
#         ans = []
#         for r, c in queries:
            
#             if rows[r] or cols[c] or diags[r-c] or anti_diags[r+c]:
#                 ans.append(1)
#             else:
#                 ans.append(0)
#             for dr in range(-1,2):
#                 for dc in range(-1,2):
#                     dr += r 
#                     dc += c 
#                     if (dr,dc) in seen:
#                         seen.remove((dr,dc))
#                         rows[dr] -= 1
#                         cols[dc] -= 1
#                         diags[dr-dc] -= 1
#                         anti_diags[dr+dc] -= 1
#         return ans


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row, col, diag, antidiag = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        delta = [-1,0,1]
        online = set()
        for r, c in lamps:
            if (r,c) not in online:
                online.add((r,c))
                row[r] += 1
                col[c] += 1
                diag[r-c] += 1
                antidiag[r+c] += 1
        ans = []
        # print(online)
        for r, c in queries:
            if row[r] or col[c] or diag[r-c] or antidiag[r+c]:
                ans.append(1)
            else:
                ans.append(0)
            for dr in delta:
                for dc in delta:
                    rr = r + dr 
                    cc = c + dc  
                    if (rr,cc) in online:
                        online.remove((rr,cc))
                        row[rr] -= 1
                        col[cc] -= 1
                        diag[rr-cc] -= 1
                        antidiag[rr+cc] -= 1
            # print(online,row,col,diag,antidiag)
        return ans
