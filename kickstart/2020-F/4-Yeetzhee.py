import os,sys
from random import randint, shuffle
from io import BytesIO, IOBase

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
from functools import lru_cache
from itertools import accumulate, permutations
import math, copy


# Fast IO Region
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

MOD = 998244353 


# https://leetcode.cn/contest/ubiquant2022/ranking/

def main():

    def solve(nums, kind):
        nums.sort(reverse=True)
        while len(nums) < kind:
            nums.append(0)
        nums = tuple(nums)

        @lru_cache(None)
        def dfs(s):
            if s == nums:
                return 0
            state = list(s)
            E = 0
            vain = 0
            for i in range(len(state)):
                new_state = copy.copy(state)
                new_state[i] += 1
                new_state.sort(reverse=True)
                new_state = tuple(new_state)
                if not all(new_state[j] <= nums[j] for j in range(kind)):
                    vain += 1 / kind
                    continue
                E += (dfs(new_state) + 1) / kind
            return (vain + E) / (1 - vain)

        return dfs(tuple([0] * kind))


# 作者：长夜
# 链接：https://leetcode.cn/circle/article/l8SRYI/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    t = int(input())
    # t = 1
    for i in range(t):
        _, kind, n = list(map(int, input().split()))
        nums = []
        for _ in range(n):
            nums.append(int(input()))
        
        res = solve(nums,kind)
        print("Case #{}: {}".format(str(i+1), str(res)))


    # debug(ans)


if __name__ == "__main__":
    main()


