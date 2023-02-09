class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)+1
        tot = reduce(lambda a, b: a^b, range(1,n+1), 0)
        cur = 0
        for i in range(1,n-1,2):
            cur ^= encoded[i]
        perm = [0]*n
        perm[0] = tot^cur
        for i in range(1,n):
            perm[i] = perm[i-1]^encoded[i-1]
        return perm



class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        sums, n = 0, len(encoded)
        for i in range(1,n+2):
            sums ^= i 
        for i in range(1,n,2):
            sums ^= encoded[i]
        res = [0]*(n+1)
        res[0] = sums
        for i in range(1,n+1):
            res[i] = res[i-1]^encoded[i-1]
        return res 
