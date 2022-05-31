class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def conv(s):
            hh, mm = s.split(':')
            t = int(hh)*60+int(mm)
            return t 
        ans = 0 
        delta = conv(correct)-conv(current)
        steps = [60,15,5,1]
        for d in steps:
            ans += delta//d
            delta %= d
        return ans