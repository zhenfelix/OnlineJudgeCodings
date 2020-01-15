class Solution:
    def getNoZeroIntegers(self, n):
        for a in range(1, n):
            b = n - a
            if '0' not in f'{a}{b}':
                return [a, b]


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def dfs(x):
            if x == 19:
                return 1
            if x < 19:
                return x//2
            cur = x%10
            if cur < 2:
                return (10+cur)//2+dfs(x//10-1)*10
            else:
                return cur//2+dfs(x//10)*10
        a = dfs(n)
        return [a,n-a]
        