class Solution:
    def smallestValue(self, n: int) -> int:
        def calc(x):
            ans = 0
            f = 2
            m = x 
            while f*f <= x:
                if m%f == 0:
                    while m%f == 0:
                        m //= f 
                        ans += f 
                f += 1  
            if m > 1:
                ans += m 
            return ans 

        pre = n 
        while 1:
            cur = calc(pre)
            if cur == pre:
                return cur
            pre = cur 

        return -1 

