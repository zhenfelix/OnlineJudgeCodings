class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0]*n 
        left, right = 0, 0 
        ans = n 
        for i in range(1,n):
            if i <= right:
                z[i] = min(z[i-left], right-i+1)
            while i+z[i] < n and s[z[i]] == s[i+z[i]]:
                z[i] += 1
            if i+z[i]-1 > right:
                left, right = i, i+z[i]-1
            ans += z[i]
        return ans


from typing import Sequence

class Solution:
    def sumScores(self, s: str) -> int:
        def countPre(curLen: int, start: int) -> int:
            left, right = 1, curLen
            while left <= right:
                mid = (left + right) // 2
                if hasher.getHashOfSlice(start, start + mid) == hasher.getHashOfSlice(0, mid):
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        n = len(s)
        StringHasher.setMOD(151217133020331712151)
        hasher = StringHasher(s)

        res = 0
        for i in range(1, n + 1):
            if s[-i] != s[0]:
                continue
            count = countPre(i, n - i)
            res += count
        return res


class StringHasher:
    _BASE = 131
    _MOD = 2 ** 64
    _OFFSET = 96

    @staticmethod
    def setBASE(base: int) -> None:
        StringHasher._BASE = base

    @staticmethod
    def setMOD(mod: int) -> None:
        StringHasher._MOD = mod

    @staticmethod
    def setOFFSET(offset: int) -> None:
        StringHasher._OFFSET = offset

    def __init__(self, sequence: Sequence[str]):
        self._sequence = sequence
        self._prefix = [0] * (len(sequence) + 1)
        self._base = [0] * (len(sequence) + 1)
        self._prefix[0] = 0
        self._base[0] = 1
        for i in range(1, len(sequence) + 1):
            self._prefix[i] = (
                self._prefix[i - 1] * StringHasher._BASE + ord(sequence[i - 1]) - self._OFFSET
            ) % StringHasher._MOD
            self._base[i] = (self._base[i - 1] * StringHasher._BASE) % StringHasher._MOD

    def getHashOfSlice(self, left: int, right: int) -> int:
        """s[left:right]的哈希值"""
        assert 0 <= left <= right <= len(self._sequence)
        left += 1
        upper = self._prefix[right]
        lower = self._prefix[left - 1] * self._base[right - (left - 1)]
        return (upper - lower) % StringHasher._MOD



作者：981377660LMT
链接：https://leetcode.cn/problems/sum-of-scores-of-built-strings/solution/ts-er-fen-zi-fu-chuan-ha-xi-by-981377660-u7i4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。