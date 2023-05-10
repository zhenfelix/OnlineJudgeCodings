class FrequencyTracker:
    def __init__(self):
        self.cnt = Counter()  # 每个数的出现次数
        self.freq = Counter()  # 出现次数的出现次数

    def add(self, number: int) -> None:
        self.freq[self.cnt[number]] -= 1  # 直接减，因为下面询问的不会涉及到 frequency=0
        self.cnt[number] += 1
        self.freq[self.cnt[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.cnt[number] == 0: return  # 不删除任何内容
        self.freq[self.cnt[number]] -= 1
        self.cnt[number] -= 1
        self.freq[self.cnt[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0


作者：endlesscheng
链接：https://leetcode.cn/problems/frequency-tracker/solution/shuang-ha-xi-biao-o1-zuo-fa-pythonjavacg-jo68/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class FrequencyTracker:

    def __init__(self):
        self.freq = Counter()
        self.cc = Counter()

    def add(self, number: int) -> None:
        # print("add",number)
        if self.freq[number] > 0:
            self.cc[self.freq[number]] -= 1
        self.freq[number] += 1
        self.cc[self.freq[number]] += 1


    def deleteOne(self, number: int) -> None:
        # print("delete",number)
        if self.freq[number] > 0:
            self.cc[self.freq[number]] -= 1
        else:
            return
        self.freq[number] -= 1
        self.cc[self.freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        # print("freq",frequency)
        # print(self.cc,self.freq)
        return self.cc[frequency] > 0



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)