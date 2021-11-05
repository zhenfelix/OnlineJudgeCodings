class StockSpanner:

#     def __init__(self):
#         self.day = 1
#         self.st = [(float('inf'),0)]

#     def next(self, price: int) -> int:
#         while self.st[-1][0] <= price:
#             self.st.pop()
#         res = self.day-self.st[-1][1]
#         self.st.append((price,self.day))
#         self.day += 1
#         return res
        


# # Your StockSpanner object will be instantiated and called as such:
# # obj = StockSpanner()
# # param_1 = obj.next(price)


    def __init__(self):
        self.stack = []

    def next(self, price):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res