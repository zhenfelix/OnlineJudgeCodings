class Solution:
    def nextClosestTime(self, time: str) -> str:
        def isValid(hours, minutes):
            hour = hours[0]*10+hours[1]
            minute = minutes[0]*10+minutes[1]
            return hour >= 0 and hour < 24 and minute >= 0 and minute < 60
        h, m = int(time.split(':')[0]), int(time.split(':')[1])
        hs = [h//10, h%10]
        ms = [m//10, m%10]
        t = hs+ms
        digits = sorted(t)
        for i in range(3,-1,-1):
            for d in digits:
                tmp = t.copy()
                tmp[i] = d
                if d > t[i] and isValid(tmp[:2], tmp[2:]):
                    t[i] = d
                    t = list(map(str,t))
                    return ':'.join([''.join(t[:2]), ''.join(t[2:])])
            t[i] = digits[0]
        t = list(map(str,t))
        return ':'.join([''.join(t[:2]), ''.join(t[2:])])