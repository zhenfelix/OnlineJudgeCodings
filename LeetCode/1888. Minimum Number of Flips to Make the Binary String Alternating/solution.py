class Solution:
    def minFlips(self, s: str) -> int:
        s = [ord(ch)-ord('0') for ch in s]
        n = len(s)
        mat = [[0,0],[0,0]]
        for i in range(n):
            mat[i&1][s[i]] += 1

        res = n 
        for i in range(n):
            res = min(res, mat[0][0]+mat[1][1])
            res = min(res, mat[0][1]+mat[1][0])
            mat[0][s[i]] -= 1
            mat[0][0], mat[1][0] = mat[1][0], mat[0][0]
            mat[0][1], mat[1][1] = mat[1][1], mat[0][1]
            mat[(n-1)&1][s[i]] += 1
        return res

