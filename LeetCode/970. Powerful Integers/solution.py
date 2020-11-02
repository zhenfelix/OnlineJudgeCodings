class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        a = 1
        while a <= bound:
            b = 1
            while a+b <= bound:
                res.add(a+b)
                b *= y
                if y == 1:
                    break
            if x == 1:
                break
            a *= x
        return list(res)