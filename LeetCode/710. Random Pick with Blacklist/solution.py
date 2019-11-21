# import random

# class Solution:

#     def __init__(self, N: int, blacklist: List[int]):
#         self.mp = {}
#         self.blacklist = set(blacklist)
#         self.N = N
        

#     def pick(self) -> int:
#         idx = random.randint(0,self.N-1)
#         if idx not in self.blacklist:
#             return idx
#         if idx in self.mp:
#             return self.mp[idx]
#         if idx == self.N-1:
#             self.N -= 1
#             return self.pick()
#         while self.N-1 in self.blacklist and self.N-1 not in self.mp:
#             self.N -= 1
#         if self.N-1 in self.mp:
#             self.mp[idx] = self.mp[self.N-1]
#         else:
#             self.mp[idx] = self.N-1
#         if self.N-1 > idx: self.N -= 1
#         return self.mp[idx]

        


# # Your Solution object will be instantiated and called as such:
# # obj = Solution(N, blacklist)
# # param_1 = obj.pick()

import random

class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.mp = {}
        self.blacklist = set(blacklist)
        M = N - len(self.blacklist)
        for b in self.blacklist:
            if b < M:
                while N-1 in self.blacklist:
                    N -= 1
                self.mp[b] = N-1
                N -= 1
        self.N = M

    def pick(self) -> int:
        idx = random.randint(0,self.N-1)
        if idx in self.mp:
            return self.mp[idx]
        return idx

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()