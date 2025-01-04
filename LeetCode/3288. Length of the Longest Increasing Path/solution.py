class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        kx, ky = coordinates[k]
        coordinates.sort(key=lambda p: (p[0], -p[1]))

        g = []
        for x, y in coordinates:
            if x < kx and y < ky or x > kx and y > ky:
                j = bisect_left(g, y)
                if j < len(g):
                    g[j] = y
                else:
                    g.append(y)
        return len(g) + 1  # 算上 coordinates[k]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/length-of-the-longest-increasing-path/solutions/2917590/pai-xu-lispythonjavacgo-by-endlesscheng-803g/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# class MyTuple:
#     def __init__(self,a,b):
#         self.a = a  
#         self.b = b  
#     def __lt__(self,other):
#         return self.a < other.a and self.b < other.b  
#     def __repr__(self):
#         return '({},{})'.format(self.a,self.b)

# class Solution:
#     def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
#         n = len(coordinates)
#         arr = []
#         for i in range(n):
#             arr.append((coordinates[i][0],-coordinates[i][1],i))
#         arr.sort()
#         ans = 0
#         st = []
#         for i in range(n):
#             x, y, j = arr[i]
#             y = -y
#             tmp = MyTuple(x,y)
#             idx = bisect.bisect_left(st,tmp)
#             if idx >= len(st):
#                 st.append(tmp)
#             else:
#                 st[idx] = tmp  
#             # print(st)
#             if j == k:
#                 ans += idx
#                 break
#         st = []
#         for i in range(n)[::-1]:
#             x, y, j = arr[i]
#             x = -x  
#             tmp = MyTuple(x,y)
#             idx = bisect.bisect_left(st,tmp)
#             if idx >= len(st):
#                 st.append(tmp)
#             else:
#                 st[idx] = tmp 
#             # print(st)
#             if j == k:
#                 ans += idx
#                 break
#         return ans+1
