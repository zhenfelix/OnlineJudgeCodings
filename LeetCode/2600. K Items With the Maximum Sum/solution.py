class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        delta = min(numOnes,k)
        ans += delta
        k -= delta
        delta = min(numZeros,k)
        k -= delta
        delta = min(numNegOnes,k)
        ans -= delta
        return ans 