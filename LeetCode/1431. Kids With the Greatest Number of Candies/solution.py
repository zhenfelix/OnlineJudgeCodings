class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        target = max(candies)
        res = []
        for c in candies:
            res.append(c+extraCandies >= target)
        return res