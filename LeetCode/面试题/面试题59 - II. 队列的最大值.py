class MaxQueue:

    def __init__(self):
        self.q = deque()
        self.mx = deque()


    def max_value(self) -> int:
        return self.mx[0] if self.mx else -1


    def push_back(self, value: int) -> None:
        self.q.append(value)
        while self.mx and self.mx[-1] < value:
            self.mx.pop()
        self.mx.append(value)


    def pop_front(self) -> int:
        if not self.q:
            return -1
        res = self.q.popleft()
        if res == self.mx[0]:
            self.mx.popleft()
        return res



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()