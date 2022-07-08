class Solution:
    def countAsterisks(self, s: str) -> int:
        if '|' not in s:
            return s.count('*')
        arr = s.split('|')
        cnt = 0
        for i, ss in enumerate(arr):
            if i%2 == 0:
                cnt += ss.count('*')
        return cnt


class Solution:
    def countAsterisks(self, s: str) -> int:
        tmp = s.split('|')[::2]
        return ''.join(tmp).count('*')