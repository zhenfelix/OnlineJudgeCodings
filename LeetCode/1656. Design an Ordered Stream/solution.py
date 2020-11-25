class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.cur = 1
        self.mp = {}


    def insert(self, id: int, value: str) -> List[str]:
        res = []
        self.mp[id] = value
        while self.cur in self.mp:
            res.append(self.mp[self.cur])
            del self.mp[self.cur]
            self.cur += 1
        return res 



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)