class ExpireList:
    __slots__ = 'lst'

    def __init__(self, lst):
        self.lst = lst

    def __lt__(self, other):
        return self.lst[1] < other.lst[1]

class Good:
    __slots__ = 'data', 'expire', 'left'

    def __init__(self):
        self.data = []
        self.expire = []
        self.left = 0

class VendingMachine:
    def __init__(self):
        self.good = defaultdict(Good)
        self.discount = defaultdict(lambda: 100)

    def addItem(self, time: int, number: int, item: str, price: int, duration: int) -> None:
        it = self.good[item]
        lst = [price, time + duration, number]
        heappush(it.data, lst)
        heappush(it.expire, ExpireList(lst))
        it.left += number

    def sell(self, time: int, customer: str, item: str, number: int) -> int:
        it = self.good[item]
        # 清除过期商品
        while it.expire and it.expire[0].lst[1] < time:
            lst = heappop(it.expire).lst
            it.left -= lst[2]
            lst[2] = 0  # 懒删除 it.data 中的元素

        if it.left < number:
            return -1
        it.left -= number

        # 计算花费
        cost = 0
        while it.data:
            lst = it.data[0]
            if lst[2] >= number:
                cost += number * lst[0]
                lst[2] -= number
                break
            cost += lst[2] * lst[0]
            number -= lst[2]
            lst[2] = 0  # 懒删除 it.expire 中的元素
            heappop(it.data)

        # 计算折扣
        ans = (cost * self.discount[customer] + 99) // 100
        if self.discount[customer] > 70:
            self.discount[customer] -= 1
        return ans


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/circle/discuss/7c1ifr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




class VendingMachine:

    def __init__(self):
        self.items = defaultdict(list)
        self.customers = dict()


    def addItem(self, time: int, number: int, item: str, price: int, duration: int) -> None:
        heapq.heappush(self.items[item], (price,time+duration,number))


    def sell(self, time: int, customer: str, item: str, number: int) -> int:
        ans = 0
        distcount = self.customers[customer] if customer in self.customers else 1
        tmp = []
        while self.items[item]:
            p, t, cnt = heapq.heappop(self.items[item])
            if t >= time:
                tmp.append((p,t,cnt))
                delta = min(number,cnt)
                ans += distcount*delta*p
                cnt -= delta
                number -= delta
                if cnt > 0:
                    heapq.heappush(self.items[item], (p,t,cnt))
                if number == 0:
                    break
        if number > 0:
            for p,t,cnt in tmp:
                heapq.heappush(self.items[item], (p,t,cnt))
            return -1
        self.customers[customer] = max(0.7,distcount-0.01)
        return ceil(ans) 



# Your VendingMachine object will be instantiated and called as such:
# obj = VendingMachine()
# obj.addItem(time,number,item,price,duration)
# param_2 = obj.sell(time,customer,item,number)