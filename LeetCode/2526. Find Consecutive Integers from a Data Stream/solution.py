class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k 
        self.q = deque()
        self.cnt = 0


    def consec(self, num: int) -> bool:
        self.q.append(num)
        if num == self.value:
            self.cnt += 1
        if len(self.q) > self.k:
            num = self.q.popleft()
            if num == self.value:
                self.cnt -= 1
        return self.cnt == self.k




# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)