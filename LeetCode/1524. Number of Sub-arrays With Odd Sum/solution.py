class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = odd = even = 0
        for x in arr:
            even += 1
            if x % 2:
                odd, even = even, odd
            res = (res + odd) % 1000000007             
        return res       



class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cc = [1,0]
        cur, sums = 0, 0
        Mod = 10**9+7
        for a in arr:
            cur += a 
            sums += cc[1-(cur&1)]
            sums %= Mod
            cc[cur&1] += 1
        return sums
