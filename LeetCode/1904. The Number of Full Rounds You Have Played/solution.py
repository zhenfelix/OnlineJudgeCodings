class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        def convert(time):
            hh, mm = map(int, time.split(':'))
            return hh*60+mm
        s, f = convert(startTime), convert(finishTime)
        if f < s:
            f += 24*60
        rs, rf = (s-1)//15+1, f//15
        return max(rf-rs,0)
        # return rf-rs
        # "00:16"
        # "00:17"