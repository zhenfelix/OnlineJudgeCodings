class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        ans = 0
        rows = [0]*n 
        cols = [0]*n 
        cntr = cntc = 0
        for t,idx,v in queries[::-1]:
            if t == 0:
                if rows[idx] == 0:
                    rows[idx] = 1
                    cntr += 1
                    ans += (n-cntc)*v 
            else:
                if cols[idx] == 0:
                    cols[idx] = 1
                    cntc += 1
                    ans += (n-cntr)*v 
        return ans 