class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        changes = [0]*(n+1)
        cnt, res = 0, 0
        for i, a in enumerate(A):
            cnt += changes[i]
            a += cnt
            a %= 2
            if a == 0:
                if i+K > n:
                    return -1
                changes[i] += 1
                changes[i+K] -= 1
                cnt += 1
                res += 1
        return res 
