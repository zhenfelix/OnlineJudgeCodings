class BlackBox:

    def __init__(self, n: int, m: int):
        self.n, self.m = n, m
        self.total = (n + m)*2
        self.cnt = 0
        self.pos = [(self.total - i)%self.total for i in range(self.total)]
        self.neg = [(m*2 - i)%self.total for i in range(self.total)]
        self.state = [False]*self.total


    def open(self, index: int, direction: int) -> int:
        if not self.state[index]:
            self.state[index] = True
            self.cnt += 1
        if self.cnt == 1:
            return index
        while True:
            if direction == 1:
                index = self.pos[index]
            else:
                index = self.neg[index]
            direction = -direction
            if self.state[index]:
                break
        return index


    def close(self, index: int) -> None:
        self.state[index] = False
        self.cnt -= 1



# Your BlackBox object will be instantiated and called as such:
# obj = BlackBox(n, m)
# param_1 = obj.open(index,direction)
# obj.close(index)