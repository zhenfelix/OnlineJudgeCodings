class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        p, q = numBottles//(numExchange-1), numBottles%(numExchange-1)
        return p*numExchange+q-(q==0)