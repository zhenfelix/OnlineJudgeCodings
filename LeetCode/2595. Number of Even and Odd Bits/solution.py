class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd, idx = 0, 0, 0
        while n:
            if n&1:
                if idx&1:
                    odd += 1
                else:
                    even += 1
            idx += 1
            n >>= 1
        return [even,odd]