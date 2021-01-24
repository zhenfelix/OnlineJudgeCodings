class Solution:
    def maximumTime(self, time: str) -> str:
        hh, mm = time.split(':')
        if hh == "??":
            hh = "23"
        elif hh[0] == "?":
            if hh[1] > "3":
                hh = "1"+hh[1]
            else:
                hh = "2"+hh[1]
        elif hh[1] == "?":
            if hh[0] == "2":
                hh = "23"
            else:
                hh = hh[0]+"9"
        if mm == "??":
            mm = "59"
        elif mm[0] == "?":
            mm = "5"+mm[1]
        elif mm[1] == "?":
            mm = mm[0]+"9"
        return hh+":"+mm