class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        for i in range(1,n+1):
            res += (i-1)//7+1+((i-1)%7)
        return res