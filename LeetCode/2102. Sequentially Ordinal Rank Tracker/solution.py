class minHeap:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score < other.score or (self.score == other.score and self.name > other.name)

class maxHeap:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score > other.score or (self.score == other.score and self.name < other.name)


class SORTracker:

    def __init__(self):
        self.hi, self.lo = [], []

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.hi, minHeap(name, score))
        tmp = heapq.heappop(self.hi)
        heapq.heappush(self.lo, maxHeap(tmp.name, tmp.score))


    def get(self) -> str:
        tmp = heapq.heappop(self.lo)
        heapq.heappush(self.hi, minHeap(tmp.name, tmp.score))
        return self.hi[0].name



# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()


class minHeap:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score < other.score or (self.score == other.score and self.name > other.name)

class maxHeap:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score > other.score or (self.score == other.score and self.name < other.name)


class SORTracker:

    def __init__(self):
        self.hi, self.lo = [], []

    def add(self, name: str, score: int) -> None:
        if self.hi and minHeap(name,score) > self.hi[0]:
            heapq.heappush(self.hi, minHeap(name, score))
            tmp = heapq.heappop(self.hi)
            name, score = tmp.name, tmp.score
        heapq.heappush(self.lo, maxHeap(name, score))


    def get(self) -> str:
        tmp = heapq.heappop(self.lo)
        heapq.heappush(self.hi, minHeap(tmp.name, tmp.score))
        return self.hi[0].name



# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()