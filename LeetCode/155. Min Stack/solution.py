class MinStack:

    def __init__(self):
        self.st = []
        self.stm = [float('inf')]

    def push(self, val: int) -> None:
        self.st.append(val)
        self.stm.append(min(val,self.stm[-1]))


    def pop(self) -> None:
        self.st.pop()
        self.stm.pop()


    def top(self) -> int:
        return self.st[-1]


    def getMin(self) -> int:
        return self.stm[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()