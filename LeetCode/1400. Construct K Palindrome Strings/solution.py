class Solution:
    # def canConstruct(self, s: str, k: int) -> bool:
    #     cc = Counter(s)
    #     return sum(map(lambda x:x&1,cc.values())) <= k and len(s) >= k
    
    def canConstruct(self, s, k):
        return sum(i & 1 for i in collections.Counter(s).values()) <= k <= len(s)