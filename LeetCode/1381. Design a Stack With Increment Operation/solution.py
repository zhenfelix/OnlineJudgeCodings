# class CustomStack:

#     def __init__(self, maxSize: int):
#         self.st = []
#         self.sums = defaultdict(int)
#         self.sz = maxSize

#     def push(self, x: int) -> None:
#         n = len(self.st)
#         if n < self.sz:
#             self.st.append(x)
        

#     def pop(self) -> int:
#         if not self.st:
#             return -1
#         n = len(self.st)
#         res = self.sums[n]
#         self.sums[n-1] += res
#         self.sums[n] = 0
#         return self.st.pop()+res
        

#     def increment(self, k: int, val: int) -> None:
#         n = len(self.st)
#         k = min(n,k)
#         self.sums[k] += val

class CustomStack:
    
    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.inc = [0]

    def push(self, x):
        if len(self.stack) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.stack: return -1
        self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        self.inc[min(k, len(self.stack))] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)