class FrontMiddleBackQueue(object):

    def __init__(self):
        self.A, self.B = collections.deque(), collections.deque()

    def pushFront(self, val):
        self.A.appendleft(val)
        self.balance()

    def pushMiddle(self, val):
        if len(self.A) > len(self.B):
            self.B.appendleft(self.A.pop())
        self.A.append(val)

    def pushBack(self, val):
        self.B.append(val)
        self.balance()

    def popFront(self):
        val = self.A.popleft() if self.A else -1
        self.balance()
        return val

    def popMiddle(self):
        val = (self.A or [-1]).pop()
        self.balance()
        return val

    def popBack(self):
        val = (self.B or self.A or [-1]).pop()
        self.balance()
        return val

    # keep A.size() >= B.size()
    def balance(self):
        if len(self.A) > len(self.B) + 1:
            self.B.appendleft(self.A.pop())
        if len(self.A) < len(self.B):
            self.A.append(self.B.popleft())
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()