class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        n = len(days)
        for i in range(1,n):
            days[i] += days[i-1]

        def calc(t):
            m, d = map(int, t.split('-'))
            return days[m-1]+d
        ami, amx = calc(arriveAlice), calc(leaveAlice)
        bmi, bmx = calc(arriveBob), calc(leaveBob)
        if bmi > amx or ami > bmx:
            return 0 
        mi = max(ami,bmi)
        mx = min(amx,bmx)
        return mx-mi+1