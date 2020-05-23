class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.up, self.down = [], []


    def addNum(self, num: int) -> None:
        if len(self.up) == len(self.down):
            num = -heapq.heappushpop(self.down,-num)
            heapq.heappush(self.up,num)
        else:
            num = heapq.heappushpop(self.up,num)
            heapq.heappush(self.down,-num)


    def findMedian(self) -> float:
        if len(self.up) == len(self.down):
            return (self.up[0]-self.down[0])/2
        else:
            return self.up[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()