class Solution:
    def findComplement(self, num: int) -> int:
        total = num
        pre = total
        while total:
            pre = total
            total = total & (total-1)
        return (pre<<1)-1-num