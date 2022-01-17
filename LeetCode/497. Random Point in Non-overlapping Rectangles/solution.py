class Solution:

    def __init__(self, rects: List[List[int]]):
        n = len(rects)
        presums = [0]*n 
        for i in range(n):
            a, b, x, y = rects[i]
            presums[i] += presums[i-1]+(x-a+1)*(y-b+1)
        self.presums = presums
        self.rects = rects
        

    def pick(self) -> List[int]:
        r = random.randint(1,self.presums[-1])
        idx = bisect.bisect_left(self.presums, r)
        a, b, x, y = self.rects[idx]
        return [random.randint(a,x),random.randint(b,y)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()



class Solution:
    def __init__(self, rects):
        w = [(x2-x1+1)*(y2-y1+1) for x1,y1,x2,y2 in rects]
        self.weights = [i/sum(w) for i in accumulate(w)]
        self.rects = rects

    def pick(self):
        n_rect = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[n_rect] 
        return [random.randint(x1, x2),random.randint(y1, y2)]