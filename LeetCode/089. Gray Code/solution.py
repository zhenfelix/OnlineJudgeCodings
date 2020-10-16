class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        left = self.grayCode(n-1)
        hi = 1<<(n-1)
        right = [hi|x for x in left]
        return left + right[::-1]


    def grayCode(self, n):
        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)]
        return results