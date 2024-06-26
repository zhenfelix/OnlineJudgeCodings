class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]
        self.cnt = [0]

    def add(self, num: int) -> None:
        if num == 0:
            self.cnt.append(self.cnt[-1]+1)
            self.arr.append(self.arr[-1])
        else:
            self.cnt.append(self.cnt[-1])
            self.arr.append(self.arr[-1]*num)
        # print(self.arr,self.cnt)
        

    def getProduct(self, k: int) -> int:
        n = len(self.arr)
        left, right = n-1-k, n-1
        if self.cnt[left] == self.cnt[right]:
            return self.arr[right]//self.arr[left]
        else:
            return 0


#     def __init__(self):
#         self.A = [1]

#     def add(self, a):
#         if a == 0:
#             self.A = [1]
#         else:
#             self.A.append(self.A[-1] * a)

#     def getProduct(self, k):
#         if k >= len(self.A): return 0
#         return self.A[-1] // self.A[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)