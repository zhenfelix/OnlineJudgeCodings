class Bitset:

    def __init__(self, size: int):
        self.nums = [0]*size
        self.cnt = 0
        self.reverse = 0


    def fix(self, idx: int) -> None:
        pre = self.nums[idx]^self.reverse
        self.nums[idx] = (1^self.reverse)
        self.cnt += (1-pre)


    def unfix(self, idx: int) -> None:
        pre = self.nums[idx]^self.reverse
        self.nums[idx] = self.reverse
        self.cnt += (0-pre)


    def flip(self) -> None:
        self.reverse = (1^self.reverse)
        self.cnt = len(self.nums)-self.cnt


    def all(self) -> bool:
        return self.cnt == len(self.nums)


    def one(self) -> bool:
        return self.cnt > 0


    def count(self) -> int:
        return self.cnt


    def toString(self) -> str:
        res = []
        for ch in self.nums:
            ch = (ch^self.reverse)
            res.append(str(ch))
        return ''.join(res)



# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()

