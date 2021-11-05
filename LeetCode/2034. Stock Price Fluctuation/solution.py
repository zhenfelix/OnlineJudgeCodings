class StockPrice:

    def __init__(self):
        self.now = -1
        self.mx = []
        self.mi = []
        self.record = dict()


    def update(self, timestamp: int, price: int) -> None:
        self.now = max(self.now, timestamp)
        self.record[timestamp] = price
        heapq.heappush(self.mi, (price,timestamp))
        heapq.heappush(self.mx, (-price,timestamp))


    def current(self) -> int:
        return self.record[self.now]


    def maximum(self) -> int:
        while self.mx and -self.mx[0][0] != self.record[self.mx[0][1]]:
            heapq.heappop(self.mx)
        return -self.mx[0][0]


    def minimum(self) -> int:
        while self.mi and self.mi[0][0] != self.record[self.mi[0][1]]:
            heapq.heappop(self.mi)
        return self.mi[0][0]



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()