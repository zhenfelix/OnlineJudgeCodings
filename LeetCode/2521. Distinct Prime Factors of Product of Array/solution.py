class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        fs = set()
        def calc(x):
            f = 2
            y = x
            while f*f <= x:
                if y%f == 0:
                    fs.add(f)
                    while y%f == 0:
                        y //= f 
                f += 1
            if y > 1:
                fs.add(y)
        for x in nums:
            calc(x)
        return len(fs)