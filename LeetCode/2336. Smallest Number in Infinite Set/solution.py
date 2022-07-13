class SmallestInfiniteSet:

    def __init__(self):
        self.removed = set()
        self.cur = 1


    def popSmallest(self) -> int:
        while self.cur in self.removed:
            self.cur += 1
        self.removed.add(self.cur)
        return self.cur


    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
            self.cur = min(self.cur, num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()