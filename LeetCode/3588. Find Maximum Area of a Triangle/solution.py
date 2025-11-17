# class Solution:
#     def maxArea(self, coords: List[List[int]]) -> int:
#         xmi,xmx,ymi,ymx = inf,-inf,inf,-inf
#         ans = -1
#         for x,y in coords:
#             xmi, xmx = min(xmi,x), max(xmx,x)
#             ymi, ymx = min(ymi,y), max(ymx,y)
#         mpxmi = dict()
#         mpxmx = dict()
#         mpymi = dict()
#         mpymx = dict()
#         for x,y in coords:
#             if x not in mpxmi:
#                 mpxmi[x] = y  
#             else:
#                 mpxmi[x] = min(mpxmi[x],y)
#             if x not in mpxmx:
#                 mpxmx[x] = y 
#             else:
#                 mpxmx[x] = max(mpxmx[x],y)
#             d = mpxmx[x] - mpxmi[x]
#             if d > 0:
#                 if xmi < x:
#                     ans = max(ans,(x-xmi)*d)
#                 if xmx > x:
#                     ans = max(ans,(xmx-x)*d)
#             if y not in mpymi:
#                 mpymi[y] = x  
#             else:
#                 mpymi[y] = min(mpymi[y],x)
#             if y not in mpymx:
#                 mpymx[y] = x 
#             else:
#                 mpymx[y] = max(mpymx[y],x)
#             d = mpymx[y] - mpymi[y]
#             if d > 0:
#                 if ymi < y:
#                     ans = max(ans,(y-ymi)*d)
#                 if ymx > y:
#                     ans = max(ans,(ymx-y)*d)
#         return ans 

# 手写 min max 更快
min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        ans = 0

        def calc() -> None:
            min_x, max_x = inf, 0
            min_y = defaultdict(lambda: inf)
            max_y = defaultdict(int)
            for x, y in coords:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y[x] = min(min_y[x], y)
                max_y[x] = max(max_y[x], y)

            nonlocal ans
            for x, y in min_y.items():
                ans = max(ans, (max_y[x] - y) * max(max_x - x, x - min_x))

        calc()

        for p in coords:
            p[0], p[1] = p[1], p[0]
        calc()

        return ans or -1

作者：灵茶山艾府
链接：https://leetcode.cn/problems/find-maximum-area-of-a-triangle/solutions/3705572/wei-hu-heng-zong-zuo-biao-de-zui-xiao-zh-rhdf/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。