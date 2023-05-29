class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:        
        prices.sort()
        delta = sum(prices[:2])
        return money if delta > money else money-delta