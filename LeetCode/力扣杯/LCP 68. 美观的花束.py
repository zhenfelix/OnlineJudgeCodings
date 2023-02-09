class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        MOD = 10**9+7
        res = 0
        cc = Counter()
        n = len(flowers)
        left = 0 
        for right in range(n):
            cc[flowers[right]] += 1  
            while cc[flowers[right]] > cnt:
                cc[flowers[left]] -= 1
                left += 1
            res += right-left+1
            res %= MOD
        return res
