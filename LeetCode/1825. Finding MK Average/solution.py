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