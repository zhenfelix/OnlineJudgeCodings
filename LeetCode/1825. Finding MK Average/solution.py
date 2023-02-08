class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.q = deque()
        self.maxn = 10+10**5
        self.tree_cnt = [0]*self.maxn
        self.tree_sum = [0]*self.maxn


    def addElement(self, num: int) -> None:
        m = self.m 
        self.q.append(num)
        self._add(self.tree_cnt, num, 1)
        self._add(self.tree_sum, num, num)
        if len(self.q) > m:
            num = self.q.popleft()
            self._add(self.tree_cnt, num, -1)
            self._add(self.tree_sum, num, -num)


    def calculateMKAverage(self) -> int:
        m, k = self.m, self.k 
        if len(self.q) < m:
            return -1
        left = self._find(self.tree_cnt, k)
        right = self._find(self.tree_cnt, m-k)
        left_sums = self._query(self.tree_sum,left)-(self._query(self.tree_cnt,left)-k)*left
        right_sums = self._query(self.tree_sum, right)-(self._query(self.tree_cnt,right)-(m-k))*right
        return (right_sums-left_sums)//(m-2*k)

    def _add(self, tree, x, delta):
        while x <= self.maxn:
            tree[x] += delta
            x += (x&(-x))

    def _query(self, tree, x):
        sums = 0
        while x:
            sums += tree[x]
            x -= (x&(-x))
        return sums

    def _find(self, tree, target):
        lo, hi = 0, self.maxn
        cnt = 0
        while lo <= hi:
            mid = (lo+hi)//2
            if self._query(self.tree_cnt, mid) >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo






# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()



from sortedcontainers import *
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k, self.s = m, k, 0
        self.q = deque()
        self.lo, self.mid, self.hi = SortedList(), SortedList(), SortedList()

    def __goup__(self):
        v = self.q.popleft()
        if self.lo.count(v):
            self.lo.remove(v)
            return
        if self.lo:
            w = self.lo[-1]
            self.lo.remove(w)
            self.s += w 
            self.mid.add(w)
        if self.mid.count(v):
            self.mid.remove(v)
            self.s -= v 
            return
        if self.mid:
            w = self.mid[-1]
            self.mid.remove(w)
            self.s -= w 
            self.hi.add(w)
        self.hi.remove(v)
        return


    def addElement(self, num: int) -> None:
        if len(self.q) == self.m:
            self.__goup__()
            
        v = num
        self.q.append(v)
        self.hi.add(v)
        if len(self.hi) > self.k:
            v = self.hi[0]
            self.hi.remove(v)
        else:
            return
        self.mid.add(v)
        self.s += v 
        if len(self.mid) > self.m-2*self.k:
            v = self.mid[0]
            self.mid.remove(v)
            self.s -= v 
        else:
            return
        self.lo.add(v)
        return



    def calculateMKAverage(self) -> int:
        # print(self.lo,self.mid,self.hi,self.s)
        if len(self.q) < self.m:
            return -1
        return self.s//(self.m-self.k*2)



# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()