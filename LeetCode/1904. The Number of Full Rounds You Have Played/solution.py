class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        def convert(time):
            hh, mm = map(int, time.split(':'))
            return hh*60+mm
        s, f = convert(startTime), convert(finishTime)
        if f < s:
            f += 24*60
        rs, rf = (s-1)//15+1, f//15
        return rf-rs