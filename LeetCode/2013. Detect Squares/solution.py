dxy = [[-1,-1],[-1,1],[1,-1],[1,1]]

class DetectSquares:

    def __init__(self):
        self.cc = Counter()

    def add(self, point: List[int]) -> None:
        self.cc[point[0],point[1]] += 1


    def count(self, point: List[int]) -> int:
        cc = self.cc
        res = 0
        x, y = point[0], point[1]
        for dx, dy in dxy:
            step = 1
            xx, yy = x, y 
            while 0 <= xx <= 1000 and 0 <= yy <= 1000:
                xx = x + step*dx 
                yy = y + step*dy
                if cc[xx,yy] > 0 and cc[xx,y] > 0 and cc[x,yy] > 0:
                    res += cc[xx,yy]*cc[xx,y]*cc[x,yy]
                step += 1
        return res 




# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)



class DetectSquares:

    def __init__(self):
        self.cnt = collections.Counter()


    def add(self, point: List[int]) -> None:
        self.cnt[(point[0], point[1])] += 1


    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        for xi, yi in self.cnt:
            if abs(xi - x) == abs(yi - y) and xi != x:
                if (xi, y) in self.cnt and (x, yi) in self.cnt:
                    ans += self.cnt[(xi, yi)] * self.cnt[(xi, y)] * self.cnt[(x, yi)]
        return ans



# 作者：吴自华
# 链接：https://leetcode-cn.com/circle/discuss/pmjXoM/view/BaQBMq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。