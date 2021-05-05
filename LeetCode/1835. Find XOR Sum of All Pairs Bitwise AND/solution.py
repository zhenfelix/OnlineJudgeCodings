class Tree:
    def __init__(self):
        self.cnt = [0]*32

    def insert(self, x):
        for i in range(32)[::-1]:
            flag = (x&(1<<i))
            if flag:
                self.cnt[i] += 1
            

    def query(self, x):
        sums = 0
        for i in range(32)[::-1]:
            flag = (x&(1<<i))
            if flag and self.cnt[i]&1:
                sums |= (1<<i)
        return sums

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        tree = Tree()
        res = 0
        for x in arr1:
            tree.insert(x)
        for x in arr2:
            # print(tree.query(x))
            res ^= tree.query(x)
        return res 