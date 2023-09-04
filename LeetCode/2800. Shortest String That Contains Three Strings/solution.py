class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        length, res = inf, ''
        if a in b or a in c: a = ''
        if b in a or b in c: b = ''
        if c in a or c in b: c = ''
        
        for x, y, z in permutations((a, b, c)):
            
            tmp = ''
            for i in range(min(len(x), len(y)), 0, -1):
                if x[-i:] == y[:i]: tmp = x + y[i:]; break
            else: tmp = x + y
            
            for i in range(min(len(tmp), len(z)), 0, -1):
                if tmp[-i:] == z[:i]: tmp = tmp + z[i:]; break
            else: tmp = tmp + z
            
            if len(tmp) < length or (len(tmp) == length and tmp < res):
                length = len(tmp)
                res = tmp
            
        return res


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/VZAN41/view/nakSJC/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def connect(x,y):
            if y in x:
                return x  
            n = len(x)
            for i in range(n):
                if x[i:] == y[:n-i]:
                    return x+y[n-i:]
            return x+y  
        def generate(x,y,z):
            x = connect(x,y)
            return connect(x,z)
        # print(connect("aaa","abc"))
        ans = [generate(x,y,z) for x,y,z in [[a,b,c],[a,c,b],[b,a,c],[b,c,a],[c,a,b],[c,b,a]]]
        # print(ans)
        return min(ans, key = lambda s: (len(s),s))