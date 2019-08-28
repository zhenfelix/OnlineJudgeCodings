# class SnapshotArray:

#     def __init__(self, length: int):
#         # nums = [0]*length
#         self.mp = {}
#         self.cc = 0
#         for i in range(length):
#             self.mp[self.cc,i] = 0

#     def set(self, index: int, val: int) -> None:
#         self.mp[self.cc,index] = val

#     def snap(self) -> int:
#         self.cc += 1
#         return self.cc-1

#     def get(self, index: int, snap_id: int) -> int:
#         while (snap_id, index) not in self.mp:
#             snap_id -= 1
#         return self.mp[snap_id, index]

class SnapshotArray(object):

    def __init__(self, n):
        self.A = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0
        self.n = n

    def set(self, index, val):
        self.A[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        return self.A[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)