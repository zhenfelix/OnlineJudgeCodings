class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro, sums = 1, 0
        while n:
            cur = n%10
            pro *= cur
            sums += cur
            n //= 10
        return pro-sums