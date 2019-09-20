from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.q = deque()
        self.sums = 0

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.sums -= self.q.popleft()
            self.q.append(val)
            self.sums += val
        else:
            self.sums += val
            self.q.append(val)
        return self.sums/len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)