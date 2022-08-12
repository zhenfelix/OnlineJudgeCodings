from sortedcontainers import SortedList
class NumberContainers:
    def __init__(self):
        self.lst = {}
        self.d = {}

    def change(self, index: int, number: int) -> None:
        if index in self.lst:
            self.d[self.lst[index]].remove(index)
        self.lst[index] = number
        if number not in self.d:
            self.d[number] = SortedList()
        self.d[number].add(index)

    def find(self, number: int) -> int:
        if number in self.d and len(self.d[number]) > 0:
            return self.d[number][0]
        return -1


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/6jXNsy/view/fAD43m/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class NumberContainers:

    def __init__(self):
        self.arr = dict()
        self.mp = defaultdict(list)


    def change(self, index: int, number: int) -> None:
        self.arr[index] = number
        heapq.heappush(self.mp[number], index)


    def find(self, number: int) -> int:
        while self.mp[number] and self.arr[self.mp[number][0]] != number:
            heapq.heappop(self.mp[number])
        if not self.mp[number]:
            return -1
        return self.mp[number][0]



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)