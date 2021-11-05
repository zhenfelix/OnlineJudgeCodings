class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        cc = Counter(candyType)
        n = len(candyType)
        res = 0
        return min(n//2,len(cc))