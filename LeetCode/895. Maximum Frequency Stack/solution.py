from collections import Counter

# class FreqStack:

#     def __init__(self):
#         self.st = []
#         self.cc = Counter()

#     # def push(self, x: int) -> None:
#     #     self.cc[x] += 1
#     #     tmp = []
#     #     while len(self.st) > 0 and self.st[-1][1] > self.cc[x]:
#     #         tmp.append(self.st.pop())
#     #     self.st.append((x,self.cc[x]))
#     #     while len(tmp) > 0:
#     #         self.st.append(tmp.pop())
#     #     return
    
#     def push(self, x: int) -> None:
#         self.cc[x] += 1
#         tmp = (x,self.cc[x])
#         self.st.append((None,None))
#         idx = len(self.st)-1
#         while idx > 0 and self.st[idx-1][1] > tmp[1]:
#             self.st[idx] = self.st[idx-1]
#             idx -= 1
#         self.st[idx] = tmp
#         return
        

#     def pop(self) -> int:
#         self.cc[self.st[-1][0]] -= 1
#         return self.st.pop()[0]

class FreqStack:

    def __init__(self):
        self.st = []
        self.cc = Counter()
    
    def push(self, x: int) -> None:
        idx = self.cc[x]
        if idx == len(self.st):
            self.st.append([x])
        else:
            self.st[idx].append(x)
        self.cc[x] += 1
        return
        

    def pop(self) -> int:
        res = self.st[-1].pop()
        if len(self.st[-1]) == 0:
            self.st.pop()
        self.cc[res] -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()