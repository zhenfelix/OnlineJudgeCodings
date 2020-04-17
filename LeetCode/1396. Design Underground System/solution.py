class UndergroundSystem:

    def __init__(self):
        self.mp = collections.defaultdict(list)
        self.tot = collections.defaultdict(int)
        self.cnt = collections.defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.mp[id].append(stationName)
        self.mp[id].append(t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, t1 = self.mp[id]
        self.tot[start,stationName] += t-t1
        self.cnt[start,stationName] += 1
        self.mp[id] = []
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.tot[startStation,endStation]/self.cnt[startStation,endStation]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)