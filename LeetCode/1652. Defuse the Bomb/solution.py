class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0]*n
        if k == 0:
            return res
        if k > 0:
            for i in range(n):
                res[i] = sum(code[j%n] for j in range(i+1,i+k+1))
        else:
            for i in range(n):
                res[i] = sum(code[j%n] for j in range(i+k,i))
        return res