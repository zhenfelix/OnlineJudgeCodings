class Solution:
    def numOfWays(self, n: int) -> int:
        a, b = 1, 1
        for i in range(1,n):
            a, b = 3*a+2*b, 2*a+2*b
        return (a+b)*6%(10**9+7)