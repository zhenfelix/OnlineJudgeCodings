
class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows, cols, diags, anti_diags = Counter(), Counter(), Counter(), Counter()
        seen = set()
        for r, c in lamps:
            rows[r] += 1
            cols[c] += 1
            diags[r-c] += 1
            anti_diags[r+c] += 1
            seen.add((r,c))
        # for i in range(len(rows)):
        #     print(rows[i])
        ans = []
        for r, c in queries:
            
            if rows[r] or cols[c] or diags[r-c] or anti_diags[r+c]:
                ans.append(1)
            else:
                ans.append(0)
            for dr in range(-1,2):
                for dc in range(-1,2):
                    dr += r 
                    dc += c 
                    if (dr,dc) in seen:
                        seen.remove((dr,dc))
                        rows[dr] -= 1
                        cols[dc] -= 1
                        diags[dr-dc] -= 1
                        anti_diags[dr+dc] -= 1
        return ans