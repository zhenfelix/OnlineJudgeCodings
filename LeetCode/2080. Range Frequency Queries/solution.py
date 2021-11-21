class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.mp = defaultdict(list)
        for i, a in enumerate(arr):
            self.mp[a].append(i)


    def query(self, left: int, right: int, value: int) -> int:
        lo = bisect.bisect_left(self.mp[value], left)
        hi = bisect.bisect_right(self.mp[value], right)
        return hi-lo



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

