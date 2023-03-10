class Solution:
    def minMaxDifference(self, num: int) -> int:
        def func(x,y):
            s = str(num)
            return int(s.replace(x,y))
        res = []
        for i in range(10):
            for j in range(10):
                res.append(func(str(i),str(j)))
        return max(res)-min(res)
