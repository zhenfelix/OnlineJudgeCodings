import bisect

class LogSystem:

    def __init__(self):
        self.arr = []
        self.g = {}
        a = "Year:Month:Day:Hour:Minute:Second"
        for i, gra in enumerate(a.split(":")):
            self.g[gra] = i

    def put(self, id: int, timestamp: str) -> None:
        bisect.insort_left(self.arr, (timestamp+":00", id))
        # print(self.arr)
        return

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        res = []
        idx = self.g[gra]+1
        s, e = s.split(":"), e.split(":")
        s.append("00")
        e.append("00")
        for i in range(idx,len(s)):
            s[i], e[i] = "00", "99"
        s, e = ":".join(s), ":".join(e)
        left = bisect.bisect_left(self.arr, (s,0))
        right = bisect.bisect_left(self.arr, (e,0))
        # print(s,e,left,right)
        for i in range(left, right):
            res.append(self.arr[i][-1])
        return res



        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)