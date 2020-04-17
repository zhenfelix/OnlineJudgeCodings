class Solution:
    def countLargestGroup(self, n: int) -> int:
        def func(x):
            res = 0
            while x:
                res += x%10
                x //= 10
            return res
            
        cc = Counter(map(func,range(1,n+1)))
        cc = Counter(cc.values())
        
        return cc[max(cc)]