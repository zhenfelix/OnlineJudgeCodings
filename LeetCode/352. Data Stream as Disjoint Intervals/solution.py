class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.interval = []
        

    def addNum(self, val: int) -> None:
        idx = bisect.bisect_left(self.interval, val)
        if idx > len(self.interval):
            if val == self.interval[-1] + 1:
                self.interval[-1] += 1
            else:
                self.interval.extend([val,val])
        elif idx & 1 == 0:
            if idx > 0 and val == self.interval[idx-1] + 1:
                self.interval[idx-1] += 1
                if idx < len(self.interval) and self.interval[idx-1] + 1 == self.interval[idx]:
                    self.interval = self.interval[:idx-1] + self.interval[idx+1:]
            elif idx < len(self.interval) and val >= self.interval[idx] - 1:
                self.interval[idx] = val
            else:
                self.interval = self.interval[:idx] + [val,val] + self.interval[idx:]
        return



        

    def getIntervals(self) -> List[List[int]]:
        res = []
        for i, x in enumerate(self.interval):
            if i & 1 == 0:
                res.append([])
            res[-1].append(x)
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()