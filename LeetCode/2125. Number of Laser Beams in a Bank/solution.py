class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        pre, cur = 0, 0
        cnt = 0
        for s in bank:
            cur = s.count('1')
            if cur > 0:
                cnt += cur*pre
                pre = cur
        return cnt