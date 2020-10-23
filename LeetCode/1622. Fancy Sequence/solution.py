class Fancy:

    def __init__(self):
        self.arr, self.add, self.mul = [], [0], [1]


    def append(self, val: int) -> None:
        self.arr.append(val)
        self.add.append(self.add[-1])
        self.mul.append(self.mul[-1])


    def addAll(self, inc: int) -> None:
        self.add[-1] += inc


    def multAll(self, m: int) -> None:
        self.mul[-1] *= m 
        self.add[-1] *= m


    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        # print(self.arr,self.add,self.mul)
        m, inc = self.mul[-1], self.add[-1]
        m //= self.mul[idx]
        inc -= m*self.add[idx]
        # print(m,inc)
        return (self.arr[idx]*m + inc)%(10**9+7)



# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)



class Fancy:

    def __init__(self):
        self.arr, self.add, self.mul = [], 0, 1
        self.MOD = 10**9+7


    def append(self, val: int) -> None:
        val -= self.add
        val %= self.MOD
        self.arr.append((val,self.mul))

    def addAll(self, inc: int) -> None:
        self.add += inc
        self.add %= self.MOD


    def multAll(self, m: int) -> None:
        self.mul *= m 
        self.add *= m
        # self.mul %= self.MOD
        self.add %= self.MOD


    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        # print(self.arr,self.add,self.mul)
        # print(m,inc)
        m, inc = self.mul, self.add
        a, b = self.arr[idx]
        return (a*m//b + inc)%self.MOD



# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)


class Fancy:

    def __init__(self):
        self.arr, self.add, self.mul = [], 0, 1
        self.MOD = 10**9+7

    def quick_mul(self, a, m):
        ret = 1
        while m:
            if m&1:
                ret *= a 
                ret %= self.MOD 
            a *= a 
            a %= self.MOD
            m = (m >> 1)
        return ret 

    def append(self, val: int) -> None:
        val -= self.add
        val = (val*self.quick_mul(self.mul, self.MOD-2))%self.MOD
        self.arr.append(val)

    def addAll(self, inc: int) -> None:
        self.add += inc
        self.add %= self.MOD


    def multAll(self, m: int) -> None:
        self.mul *= m 
        self.add *= m
        self.mul %= self.MOD
        self.add %= self.MOD


    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        # print(self.arr,self.add,self.mul)
        # print(m,inc)
        a, m, inc = self.arr[idx], self.mul, self.add
        return (a*m + inc)%self.MOD



# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
