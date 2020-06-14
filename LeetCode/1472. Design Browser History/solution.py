# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.st = [homepage]
#         self.end = 0
#         self.cur = 0
        

#     def visit(self, url: str) -> None:
#         self.cur += 1
#         if self.cur == len(self.st):
#             self.st.append(None)
#         self.st[self.cur] = url
#         self.end = self.cur 
        

#     def back(self, steps: int) -> str:
#         while steps > 0 and self.cur > 0:
#             steps -= 1
#             self.cur -= 1
#         return self.st[self.cur]
        

#     def forward(self, steps: int) -> str:
#         while steps > 0 and self.cur < self.end:
#             steps -= 1
#             self.cur += 1
#         return self.st[self.cur]
        


# # Your BrowserHistory object will be instantiated and called as such:
# # obj = BrowserHistory(homepage)
# # obj.visit(url)
# # param_2 = obj.back(steps)
# # param_3 = obj.forward(steps)

class BrowserHistory:

    def __init__(self, homepage: str):
        self.st = [homepage]
        self.end = 0
        self.cur = 0
        

    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur == len(self.st):
            self.st.append(None)
        self.st[self.cur] = url
        self.end = self.cur 
        

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur-steps)
        return self.st[self.cur]
        

    def forward(self, steps: int) -> str:
        self.cur = min(self.end, self.cur+steps)
        return self.st[self.cur]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)