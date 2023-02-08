class Solution:
    def minimumBoxes(self, n: int) -> int:
        def squre(x):
            return x*(x+1)//2
        def cube(x):
            return x*(x+1)*(x+2)//6
        a = bisect_right(range(n+1),n,key=cube)-1
        r = n-cube(a)
        # print(a,cube(a))
        b = bisect_left(range(n+1),r,key=squre)
        return squre(a)+b

class Solution:
    def minimumBoxes(self, n: int) -> int:
        def squre(x):
            return x*(x+1)//2
        def cube(x):
            return x*(x+1)*(x+2)//6
        lo, hi = 0, n 
        while lo <= hi:
            m = (lo+hi)//2
            if cube(m) <= n:
                lo = m + 1
            else:
                hi = m - 1
        n1 = hi
        r = n-cube(n1)
        # print(n1,cube(n1))
        lo, hi = 0, n
        while lo <= hi:
            m = (lo+hi)//2
            if squre(m) < r:
                lo = m + 1 
            else:
                hi = m - 1
        return squre(n1)+lo

# class Solution:
#     def minimumBoxes(self, n: int) -> int:
#         sums, r, c = 0, 1, -1
#         delta = defaultdict(int)
#         mp = {}
#         for k in range(1, n+1):
#             if r == 0:
#                 r, c = c+1, 0
#             else:
#                 r -= 1
#                 c += 1
#             mp[r,c] = k
#             delta[k] += 1
#             if c > 0:
#                 delta[k] += delta[mp[r,c-1]]
#             sums += delta[k]
#             if sums >= n:
#                 return k
#         return -1

# class Solution:
#     def minimumBoxes(self, n: int) -> int:
#         # ---------- 计算可以堆放的最大层数 ----------
#         level = 1
#         cell = 0
#         while cell + (1 + level) * level // 2 <= n:
#             cell += (1 + level) * level // 2
#             level += 1
#         level -= 1

#         # 计算当前占地面积（即最下层的盒子数量）
#         area = (1 + level) * level // 2

#         # ---------- 计算还需要继续放置的砖块 ----------
#         now = 0
#         while cell < n:
#             area += 1
#             cell += now + 1
#             now += 1

#         return area


# 使用二分法，目的只是为了少写几个IF = =||
def fbisect_left(fun,val, l, r):
    while(l<r):
        m = (l+r)//2
        if fun(m)<val: l = m+1
        else: r = m
    return l

class Solution:
    def minimumBoxes(self, n: int) -> int:
        # 从墙角出发，和墙角距离相等的方块视为“一层（layer）”。

        # 层数和占地面积的关系：
        def get2d(l):
            # 1+2+3+.....+l
            return l*(l+1)//2
        
        # 层数和方块数的关系：
        def get3d(l):
            # get2d(1)+get2d(2)+get2d(3)+.....+get2d(l)
            return l*(l+1)*(l+2)//6
        
        # 找到最大层数：
        estimate = int((n*6)**(1/3)) - 1
        targetLayer = fbisect_left(get3d, n, estimate-1, estimate+2);
        
        size = get2d(targetLayer-1)
        V = get3d(targetLayer-1)
        
        # 找到未满层的行数
        estimate = int(((n-V)*2)**0.5)
        rows = fbisect_left(get2d, n-V, estimate-1, estimate+2)
        return size + rows


class Solution:
    def minimumBoxes(self, n: int) -> int:
        lo, hi = 1, n
        def calc(k):
            sums, cur, rank = 0, 0, 1
            while True:
                if cur + rank > k:
                    break
                cur += rank
                sums += cur
                rank += 1
            remain = k - cur
            sums += (1+remain)*remain//2
            return sums


        while lo <= hi:
            mid = (lo+hi)//2
            # print(mid)
            if calc(mid) >= n:
                hi = mid-1
            else:
                lo = mid+1
        
        return lo

