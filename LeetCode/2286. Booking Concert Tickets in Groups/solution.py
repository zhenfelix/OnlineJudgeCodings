class BookMyShow:
    def update(self, arr, idx, val):
        nmax = len(arr)
        while idx < nmax:
            arr[idx] += val
            idx += idx&(-idx)

    def query(self, arr, idx):
        tot = 0
        while idx > 0:
            tot += arr[idx]
            idx -= idx&(-idx)
        return tot

    def __init__(self, n: int, m: int):
        self.n = n 
        self.m = m
        self.mi = 0
        self.cnt = [0]*n 
        sq = int(sqrt(n))
        self.qs = []
        for i in range(n):
            if i%sq == 0:
                self.qs.append([])
            self.qs[-1].append((self.cnt[i],i))
        self.sums_arr = [0]*(n+10)


    def gather(self, k: int, maxRow: int) -> List[int]:
        n, m = self.n, self.m
        sq = int(sqrt(n))
        mx = maxRow//sq
        # print(mx,sq)
        for i in range(mx+1):
            while self.qs[i] and self.cnt[self.qs[i][0][1]] > self.qs[i][0][0]:
                heapq.heappop(self.qs[i])
            if self.qs[i] and m-self.qs[i][0][0] >= k:                
                for j in range(i*sq, min(i*sq+sq, maxRow+1)):
                    if m-self.cnt[j] >= k:
                        candidates = [j, self.cnt[j]]
                        self.cnt[j] += k 
                        heapq.heappush(self.qs[i], (self.cnt[j], j))
                        self.update(self.sums_arr, j+1, k)
                        return candidates
        return []




    def scatter(self, k: int, maxRow: int) -> bool:
        n, m = self.n, self.m 
        sq = int(sqrt(n))
        lo, hi = self.mi, maxRow
        while lo <= hi:
            mid = (lo+hi)//2
            tot = m*(mid+1)-self.query(self.sums_arr, mid+1)
            if tot >= k:
                hi = mid-1
            else:
                lo = mid+1
        if lo > maxRow:
            return False
        for i in range(self.mi,lo+1):
            delta = min(k, m-self.cnt[i])
            k -= delta
            self.cnt[i] += delta
            heapq.heappush(self.qs[i//sq], (self.cnt[i],i))
            self.update(self.sums_arr,i+1,delta)
        self.mi = lo
        return True





# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)




class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.min = [0] * (n * 4)
        self.sum = [0] * (n * 4)

    # 将 idx 上的元素值增加 val
    def add(self, o: int, l: int, r: int, idx: int, val: int):
        if l == r:
            self.min[o] += val
            self.sum[o] += val
            return
        m = (l + r) // 2
        if idx <= m: self.add(o * 2, l, m, idx, val)
        else: self.add(o * 2 + 1, m + 1, r, idx, val)
        self.min[o] = min(self.min[o * 2], self.min[o * 2 + 1])
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]

    # 返回区间 [L,R] 内的元素和
    def query_sum(self, o: int, l: int, r: int, L: int, R: int):
        if L <= l and r <= R: return self.sum[o]
        sum = 0
        m = (l + r) // 2
        if L <= m: sum += self.query_sum(o * 2, l, m, L, R)
        if R > m: sum += self.query_sum(o * 2 + 1, m + 1, r, L, R)
        return sum

    # 返回区间 [1,R] 中 <= val 的最靠左的位置，不存在时返回 0
    def index(self, o: int, l: int, r: int, R: int, val: int):
        if self.min[o] > val: return 0  # 说明整个区间的元素值都大于 val
        if l == r: return l
        m = (l + r) // 2
        if self.min[o * 2] <= val: return self.index(o * 2, l, m, R, val)  # 看看左半部分
        if m < R: return self.index(o * 2 + 1, m + 1, r, R, val)  # 看看右半部分
        return 0

    def gather(self, k: int, maxRow: int) -> List[int]:
        i = self.index(1, 1, self.n, maxRow + 1, self.m - k)
        if i == 0: return []
        seats = self.query_sum(1, 1, self.n, i, i)
        self.add(1, 1, self.n, i, k)  # 占据 k 个座位
        return [i - 1, seats]

    def scatter(self, k: int, maxRow: int) -> bool:
        if (maxRow + 1) * self.m - self.query_sum(1, 1, self.n, 1, maxRow + 1) < k:
            return False  # 剩余座位不足 k 个
        i = self.index(1, 1, self.n, maxRow + 1, self.m - 1)  # 从第一个没有坐满的排开始占座
        while True:
            left_seats = self.m - self.query_sum(1, 1, self.n, i, i)
            if k <= left_seats:  # 剩余人数不够坐后面的排
                self.add(1, 1, self.n, i, k)
                return True
            k -= left_seats
            self.add(1, 1, self.n, i, left_seats)
            i += 1


作者：endlesscheng
链接：https://leetcode.cn/problems/booking-concert-tickets-in-groups/solution/by-endlesscheng-okcu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。