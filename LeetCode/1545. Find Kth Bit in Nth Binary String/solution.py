class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        mid = (2**n)//2
        if k == mid:
            return '1'
        elif k < mid:
            return self.findKthBit(n-1,k)
        else:
            k = mid*2-k
            pre = self.findKthBit(n-1,k)
            return '1' if pre == '0' else '0'